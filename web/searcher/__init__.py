"""
This is a module to load a neural network model and initialize the search space.
The necessary files to reload a trained model is stored in data directory.
It includes: the vocabulary of inputs, the vocabulary of outputs, sentence
candidates stored in csv format, and model stored in .pt extension.
The vocabularies are necessary to map words into unique numbers.
During initialization, the object numericalize sentences stored as strings in
a csv file.

The object, search_space, will be imported into web/main.py.
"""
from zencorpora.rnn_search import SearchSpace

from sentence_suggestion.inference_model import NNModel
from sentence_suggestion.inference_model import DataLoader

from torch.nn.functional import log_softmax

import os

data_dir = os.path.join('web', 'searcher', 'data')

INPUT_VOCAB_PATH = os.path.join(data_dir, 'MASKED_TEXT.Field')
OUTPUT_VOCAB_PATH = os.path.join(data_dir, 'TARGET_TEXT.Field')
DEVICE_TYPE = 'cpu'
SENTENCE_CANDIDATES_PATH = os.path.join(data_dir, 'search_space.csv')

loader = DataLoader()
model = NNModel(input_vocab_path=INPUT_VOCAB_PATH,
                output_vocab_path=OUTPUT_VOCAB_PATH,
                device_type=DEVICE_TYPE)

search_space = SearchSpace(
    src_field=model.input_field,
    trg_field=model.output_field,
    encoder=model.encoder,
    decoder=model.decoder,
    corpus_path=SENTENCE_CANDIDATES_PATH,
    hide_progress=False,
    score_function=log_softmax,
    device=model.device,
)
