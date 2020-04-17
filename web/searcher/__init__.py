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
from sentence_suggestion import inference
import os

data_dir = os.path.join('web', 'searcher', 'data')

INPUT_VOCAB_PATH = os.path.join(data_dir, 'MASKED_TEXT.Field')
OUTPUT_VOCAB_PATH = os.path.join(data_dir, 'TARGET_TEXT.Field')
MODEL_PATH = os.path.join(data_dir, 'seq2seq-multilayer-gru.pt')
DEVICE_TYPE = 'cpu'
SENTENCE_CANDIDATES_PATH = os.path.join(data_dir, 'space_sample.csv')

search_space = inference.SearchSpace(
    input_vocab_path=INPUT_VOCAB_PATH,
    output_vocab_path=OUTPUT_VOCAB_PATH,
    model_path=MODEL_PATH,
    device_type=DEVICE_TYPE,
    sentence_candidates_path=SENTENCE_CANDIDATES_PATH,
)
