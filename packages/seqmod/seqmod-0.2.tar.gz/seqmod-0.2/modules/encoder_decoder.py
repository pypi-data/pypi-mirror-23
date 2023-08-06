
import logging
import re

import numpy as np

import torch
import torch.nn as nn
from torch.autograd import Variable


from seqmod.modules.custom import word_dropout
from seqmod.modules.encoder import Encoder
from seqmod.modules.decoder import Decoder
from seqmod.misc.beam_search import Beam
from seqmod import utils as u


class EncoderDecoder(nn.Module):
    """
    Vanilla configurable encoder-decoder architecture

    Parameters:
    -----------
    num_layers: tuple(enc_num_layers, dec_num_layers) or int,
        Number of layers for both the encoder and the decoder.
    emb_dim: int, embedding dimension
    hid_dim: int, Hidden state size for the encoder and the decoder
    att_dim: int, Hidden state for the attention network.
        Note that it has to be equal to the encoder/decoder hidden
        size when using GlobalAttention.
    src_dict: Dict, A fitted Dict used to encode the data into integers.
    trg_dict: Dict, Same as src_dict in case of bilingual training.
    cell: string, Cell type to use. One of (LSTM, GRU).
    att_type: string, Attention mechanism to use. One of (Global, Bahdanau).
    dropout: float
    word_dropout: float
    bidi: bool, Whether to use bidirectional.
    add_prev: bool,
        Whether to feed back the last decoder state as input to
        the decoder for the next step together with the last
        predicted word embedding.
    init_hidden: one of 'last', 'project', optional
        Whether to use the last layer or an extra projection
        of the last encoder hidden state to initialize decoder hidden state.
    """
    def __init__(self,
                 num_layers,
                 emb_dim,
                 hid_dim,
                 att_dim,
                 src_dict,
                 trg_dict=None,
                 cell='LSTM',
                 att_type='Bahdanau',
                 dropout=0.0,
                 word_dropout=0.0,
                 maxout=0,
                 bidi=True,
                 add_prev=True,
                 tie_weights=False,
                 init_hidden='last'):
        super(EncoderDecoder, self).__init__()
        if isinstance(num_layers, tuple):
            enc_num_layers, dec_num_layers = num_layers
        else:
            enc_num_layers, dec_num_layers = num_layers, num_layers
        self.cell = cell
        self.add_prev = add_prev
        self.src_dict = src_dict
        self.trg_dict = trg_dict or src_dict
        src_vocab_size = len(self.src_dict)
        trg_vocab_size = len(self.trg_dict)
        self.bilingual = bool(trg_dict)

        # word_dropout
        self.word_dropout = word_dropout
        self.target_code = self.src_dict.get_unk()
        self.reserved_codes = (self.src_dict.get_eos(),
                               self.src_dict.get_bos(),
                               self.src_dict.get_pad())

        # embedding layer(s)
        self.src_embeddings = nn.Embedding(
            src_vocab_size, emb_dim, padding_idx=self.src_dict.get_pad())
        if self.bilingual:
            self.trg_embeddings = nn.Embedding(
                trg_vocab_size, emb_dim, padding_idx=self.trg_dict.get_pad())
        else:
            self.trg_embeddings = self.src_embeddings

        # encoder
        self.encoder = Encoder(
            emb_dim, hid_dim, enc_num_layers,
            cell=cell, bidi=bidi, dropout=dropout)

        # decoder
        self.decoder = Decoder(
            emb_dim, hid_dim, (enc_num_layers, dec_num_layers), cell, att_dim,
            dropout=dropout, maxout=maxout, add_prev=add_prev,
            init_hidden=init_hidden, att_type=att_type)

        # output projection
        output_size = trg_vocab_size if self.bilingual else src_vocab_size
        if tie_weights:
            project = nn.Linear(emb_dim, output_size)
            project.weight = self.trg_embeddings.weight
            if emb_dim != hid_dim:
                logging.warn("When tying weights, output layer and " +
                             "embedding layer should have equal size. " +
                             "A projection layer will be insterted.")
                project_tied = nn.Linear(hid_dim, emb_dim)
                self.project = nn.Sequential(
                    project_tied, project, nn.LogSoftmax())
            else:
                self.project = nn.Sequential(project, nn.LogSoftmax())
        else:
            self.project = nn.Sequential(
                nn.Linear(hid_dim, output_size),
                nn.LogSoftmax())

    # General utility functions
    def is_cuda(self):
        """
        Whether the model is on a gpu. We assume no device sharing.
        """
        return next(self.parameters()).is_cuda

    def parameters(self):
        for p in super(EncoderDecoder, self).parameters():
            if p.requires_grad is True:
                yield p

    def n_params(self):
        return sum([p.nelement() for p in self.parameters()])

    # Initializers
    def init_encoder(self, model, layer_map={'0': '0'}, target_module='rnn'):
        merge_map = {}
        for p in model.state_dict().keys():
            if not p.startswith(target_module):
                continue
            from_layer = ''.join(filter(str.isdigit, p))
            if from_layer not in layer_map:
                continue
            s = p.replace(target_module, 'encoder.rnn') \
                 .replace(from_layer, layer_map[from_layer])
            merge_map[p] = s
        state_dict = u.merge_states(
            self.state_dict(), model.state_dict(), merge_map)
        self.load_state_dict(state_dict)

    def init_decoder(self, model, target_module='rnn', layers=(0,)):
        assert isinstance(model.rnn, type(self.decoder.rnn_step))
        target_rnn = getattr(model, target_module).state_dict().keys()
        source_rnn = self.decoder.rnn_step.state_dict().keys()
        merge_map = {}
        for param in source_rnn:
            try:
                # Decoder has format "LSTMCell_0.weight_ih"
                num, suffix = re.findall(r".*([0-9]+)\.(.*)", param)[0]
                # LM rnn has format "weight_ih_l0"
                target_param = suffix + "_l" + num
                if target_param in target_rnn:
                    merge_map[target_param] = "decoder.rnn_step." + param
            except IndexError:
                continue        # couldn't find target module
        state_dict = u.merge_states(
            self.state_dict(), model.state_dict(), merge_map)
        self.load_state_dict(state_dict)

    def init_embedding(self, model,
                       source_module='src_embeddings',
                       target_module='embeddings'):
        state_dict = u.merge_states(
            model.state_dict(), self.state_dict(),
            {target_module: source_module})
        self.load_state_dict(state_dict)

    def load_embeddings(self, weight, words,
                        target_embeddings='src', verbose=False):
        """
        Load embeddings from a weight matrix with words `words` as rows.

        Parameters
        -----------
        weight: (vocab x emb_dim)
        words: list of words corresponding to each row in `weight`
        """
        if isinstance(weight, np.ndarray):
            weight = torch.from_numpy(weight)
        assert weight.size(1) == self.emb_dim, \
            "Mismatched embedding dim %d for model with dim %d" % \
            (weight.size(1), self.emb_dim)
        target_words = {word: idx for idx, word in enumerate(words)}
        for idx, word in enumerate(self.src_dict.vocab):
            if word not in target_words:
                if verbose:
                    logging.warn("Couldn't find word [%s]" % word)
                continue
            if target_embeddings == 'src':
                self.src_embeddings.weight.data[idx, :].copy_(
                    weight[target_words[word], :])
            elif target_embeddings == 'trg':
                self.trg_embeddings.weight.data[idx, :].copy_(
                    weight[target_words[word], :])
            else:
                raise ValueError('target_embeddings must be `src` or `trg`')

    def init_batch(self, src):
        """
        Constructs a first prev batch for initializing the decoder.
        """
        batch, bos = src.size(1), self.src_dict.get_bos()
        return src.data.new(1, batch).fill_(bos)

    def freeze_submodule(self, module):
        for p in getattr(self, module).parameters():
            p.requires_grad = False

    def forward(self, inp, trg):
        """
        Parameters:
        -----------
        inp: torch.Tensor (seq_len x batch), Train data for a single batch.
        trg: torch.Tensor (seq_len x batch), Target output for a single batch.

        Returns: outs, att_weights
        --------
        outs: torch.Tensor (seq_len x batch x hid_dim)
        att_weights: (batch x seq_len x target_len)
        """
        # encoder
        inp = word_dropout(
            inp, self.target_code, reserved_codes=self.reserved_codes,
            p=self.word_dropout, training=self.training)
        emb_inp = self.src_embeddings(inp)
        enc_outs, enc_hidden = self.encoder(emb_inp)
        # decoder
        dec_hidden = self.decoder.init_hidden_for(enc_hidden)
        dec_outs, dec_out, enc_att = [], None, None
        if self.decoder.att_type == 'Bahdanau':
            # cache encoder att projection for bahdanau
            enc_att = self.decoder.attn.project_enc_outs(enc_outs)
        for prev in trg.chunk(trg.size(0)):
            emb_prev = self.trg_embeddings(prev).squeeze(0)
            dec_out, dec_hidden, att_weight = self.decoder(
                emb_prev, dec_hidden, enc_outs, out=dec_out, enc_att=enc_att)
            dec_outs.append(dec_out)
        return torch.stack(dec_outs)

    def translate(self, src, max_decode_len=2):
        """
        Translate a single input sequence using greedy decoding..

        Parameters:
        -----------

        src: torch.LongTensor (seq_len x 1)
        """
        pad = self.src_dict.get_pad()
        eos = self.src_dict.get_eos()
        bos = self.src_dict.get_bos()
        gpu = src.is_cuda
        # encode
        emb = self.src_embeddings(src)
        enc_outs, enc_hidden = self.encoder(
            emb, compute_mask=False, mask_symbol=pad)
        # decode
        dec_hidden = self.decoder.init_hidden_for(enc_hidden)
        dec_out, enc_att = None, None
        if self.decoder.att_type == 'Bahdanau':
            enc_att = self.decoder.attn.project_enc_outs(enc_outs)
        scores, hyp, atts = [], [], []
        prev = Variable(src.data.new([bos]), volatile=True).unsqueeze(0)
        if gpu: prev = prev.cuda()
        for _ in range(len(src) * max_decode_len):
            prev_emb = self.trg_embeddings(prev).squeeze(0)
            dec_out, dec_hidden, att_weights = self.decoder(
                prev_emb, dec_hidden, enc_outs, out=dec_out, enc_att=enc_att)
            # (batch x vocab_size)
            outs = self.project(dec_out)
            # (1 x batch) argmax over log-probs (take idx across batch dim)
            best_score, prev = outs.max(1)
            prev = prev.t()
            # concat of step vectors along seq_len dim
            scores.append(best_score.squeeze().data[0])
            atts.append(att_weights.squeeze().data.cpu().numpy().tolist())
            hyp.append(prev.squeeze().data[0])
            # termination criterion: decoding <eos>
            if prev.data.eq(eos).nonzero().nelement() > 0:
                break
        # add singleton dimension for compatibility with other decoding
        return [sum(scores)], [hyp], [atts]

    def translate_beam(self, src, max_decode_len=2, beam_width=5):
        """
        Translate a single input sequence using beam search.

        Parameters:
        -----------

        src: torch.LongTensor (seq_len x 1)
        """
        pad = self.src_dict.get_pad()
        eos = self.src_dict.get_eos()
        bos = self.src_dict.get_bos()
        gpu = src.is_cuda
        # encode
        emb = self.src_embeddings(src)
        enc_outs, enc_hidden = self.encoder(
            emb, compute_mask=False, mask_symbol=pad)
        # decode
        enc_outs = enc_outs.repeat(1, beam_width, 1)
        if self.cell.startswith('LSTM'):
            enc_hidden = (enc_hidden[0].repeat(1, beam_width, 1),
                          enc_hidden[1].repeat(1, beam_width, 1))
        else:
            enc_hidden = enc_hidden.repeat(1, beam_width, 1)
        dec_hidden = self.decoder.init_hidden_for(enc_hidden)
        dec_out, enc_att = None, None
        if self.decoder.att_type == 'Bahdanau':
            enc_att = self.decoder.attn.project_enc_outs(enc_outs)
        beam = Beam(beam_width, bos, eos=eos, gpu=gpu)
        while beam.active and len(beam) < len(src) * max_decode_len:
            # add seq_len singleton dim (1 x width)
            prev_data = beam.get_current_state().unsqueeze(0)
            prev = Variable(prev_data, volatile=True)
            prev_emb = self.trg_embeddings(prev).squeeze(0)
            dec_out, dec_hidden, att_weights = self.decoder(
                prev_emb, dec_hidden, enc_outs, out=dec_out, enc_att=enc_att)
            # (width x vocab_size)
            outs = self.project(dec_out)
            beam.advance(outs.data)
            # TODO: this doesn't seem to affect the output :-s
            dec_out = u.swap(dec_out, 0, beam.get_source_beam())
            if self.cell.startswith('LSTM'):
                dec_hidden = (u.swap(dec_hidden[0], 1, beam.get_source_beam()),
                              u.swap(dec_hidden[1], 1, beam.get_source_beam()))
            else:
                dec_hidden = u.swap(dec_hidden, 1, beam.get_source_beam())
        # decode beams
        scores, hyps = beam.decode(n=beam_width)
        return scores, hyps, None  # TODO: return attention


class ForkableMultiTarget(EncoderDecoder):
    def fork_target(self, **init_opts):
        import copy
        model = copy.deepcopy(self)
        model.freeze_submodule('src_embeddings')
        model.freeze_submodule('encoder')
        model.decoder.apply(u.make_initializer(**init_opts))
        model.project.apply(u.make_initializer(**init_opts))
        return model
