import pandas as pd


def get_info(csv_full_dir='./data/full_clean.csv'):
    df = pd.read_csv('./data/full_clean.csv', sep=';')

    print('  #champ manquant à plus 50%: ', *list(df.columns[df.count() / df.shape[0] < 0.51]), sep='\n')


if __name__ == '__main__':
    get_info()
