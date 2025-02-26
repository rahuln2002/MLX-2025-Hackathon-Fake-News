import pandas as pd
import numpy as np
import yaml

params = yaml.safe_load(open("params.yaml"))["preprocess"]

def preprocess(input_path_one, input_path_two, output_path):
    df_fake = pd.read_csv(input_path_one)
    df_true = pd.read_csv(input_path_two)

    df_fake['result'] = 'fake'
    df_true['result'] = 'true'

    df = pd.concat([df_fake, df_true])

    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    preprocess(params['input_one'], params['input_two'], params['output'])