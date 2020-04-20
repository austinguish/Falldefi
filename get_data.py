import os
import pandas as pd
import numpy.random


def get_all_data(PATH):
    fs = os.listdir(PATH)
    all_data = pd.DataFrame()
    for f in fs:
        file_path = os.path.join(PATH, f)
        if 'csv' in f:
            data = pd.read_csv(file_path, index_col=False, low_memory=False)
            data = data.iloc[0:, 0:21]
            all_data = all_data.append(data)

    numpy.random.shuffle(all_data.values)
    print(all_data)

    return all_data


