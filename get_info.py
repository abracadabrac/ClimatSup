import pandas as pd


def get_info(cleaned_csv_path):
    df = pd.read_csv(cleaned_csv_path, sep=';')

    print('  #champ manquant à plus 50%: ', *list(df.columns[df.count() / df.shape[0] < 0.51]), sep='\n')


if __name__ == '__main__':
    get_info()
