import os
import pandas as pd

from text_prepare import text_prepare

column_name = ['ETABLISSEMENT_Type',
               'ETABLISSEMENT_Nom',
               'FORMATION_Nom',
               'FORMATION_Domaine',
               'FORMATION_Specialite',
               'FORMATION_Descriptif',
               'FORMATION_Niveau_de_diplme_lentree',
               'FORMATION_Niveau_de_diplme_en_sortie',
               'FORMATION_Duree_en_annees',
               'FORMATION_Total_ECTS',
               'FORMATION_Url_de_la_formation',
               'UNITE_DE_VALEUR_COURS_Questions_ENV_au_sens_large_evoquees_oui_non',
               'UNITE_DE_VALEUR_COURS_Enjeux_transition_energetiqueclimat_abordes_oui_non',
               'UNITE_DE_VALEUR_COURS_Nom_du_cours',
               'UNITE_DE_VALEUR_COURS_Notions_abordees',
               'UNITE_DE_VALEUR_COURS_Cours_optionnel_ou_obligatoire',
               'UNITE_DE_VALEUR_COURS_Nombre_de_credits_ECTS_accordes_par_ce_cours',
               'UNITE_DE_VALEUR_COURS_Duree_du_cours_en_nombre_dheures',
               'UNITE_DE_VALEUR_COURS_Mode_devaluation',
               'UNITE_DE_VALEUR_COURS_Avis_critique_sur_le_cours_et_ou_la_formation',
               'UNITE_DE_VALEUR_COURS_Formation_initiale_ou_continue',
               'UNITE_DE_VALEUR_COURS_Comptabilite']


def clean_csv(df):
    df = df[-df['ETABLISSEMENT_Nom'].isna() & -df['FORMATION_Nom'].isna()]
    df = df[-df.isin(['Nom', 'ETABLISSEMENT'])['ETABLISSEMENT_Nom']]
    df = df.applymap(text_prepare)
    df.dropna(how='all', axis=1)
    df = df[-df.isna().all(axis=1)]

    return df


def merge_csv(csv_path='./data/csv/', header=column_name):
    list_name = os.listdir(csv_path)
    list_df = []
    for name in list_name:
        file = csv_path + name
        df = pd.read_csv(file)
        if df.shape[1] == 22:
            df.columns = header
            df.drop(['UNITE_DE_VALEUR_COURS_Comptabilite',
                     'FORMATION_Url_de_la_formation'], axis=1, inplace=True)
            df = clean_csv(df)
            list_df.append(df)
        elif df.shape[1] == 21:
            df.columns = header[:-1]
            df.drop(['FORMATION_Url_de_la_formation'], axis=1, inplace=True)
            df = clean_csv(df)
            list_df.append(df)

    for df in list_df:
        print(df.iloc[1, 1], df.shape)

    df = pd.concat(list_df)

    print('full shape: ', df.shape, '\n')

    df.to_csv('./data/full.csv', sep=';', index=False)


if __name__ == '__main__':
    merge_csv(csv_path='./data/csv/', header=column_name)