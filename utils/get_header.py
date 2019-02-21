from utils.text_prepare import text_prepare

import os
import pandas as pd


def get_header(csv_dir):
    name = os.listdir(csv_dir)[0]
    file = csv_dir + name
    df = pd.read_csv(file)

    column_0 = list(df.columns)
    column_1 = list(df.loc[0])

    column_0_0 = []
    for i, c in enumerate(column_0):
        if not c.startswith('Unnamed'):
            column_0_0.append(c)
        else:
            column_0_0.append(column_0_0[i - 1])

    header = [text_prepare(c_0 + ' ' + c_1) for (c_0, c_1) in zip(column_0_0, column_1)]

    return header


if __name__ == '__main__':
    csv_dir = "../data/csv"
    header = get_header(csv_dir)

    print(header)
