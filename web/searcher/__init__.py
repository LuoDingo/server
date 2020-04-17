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
