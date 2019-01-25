import pandas as pd
import os
import glob
import csv
from xlsxwriter.workbook import Workbook

import numpy as np


def clean_csv(csv_path='./data/full.csv'):
    df = pd.read_csv(csv_path, sep=';')

    # dictionary of corresponding between names and types
    dict_Nom_Type = dict(df.groupby('ETABLISSEMENT_Nom').ETABLISSEMENT_Type.unique())  # corresponding between name and type
    new_dict_Nom_Type = {}  # delete non values in the dictionary
    for Nom, List_Type in dict_Nom_Type.items():
        new_dict_Nom_Type[Nom] = [Type for Type in List_Type if type(Type) is str][0]

    dict_Nom_Type = new_dict_Nom_Type

    # add type when it misses
    df.loc[df.ETABLISSEMENT_Type.isna(), 'ETABLISSEMENT_Type'] = [dict_Nom_Type[Nom] for Nom in
                                                                  list(df[df.ETABLISSEMENT_Type.isna()].ETABLISSEMENT_Nom)]
    # normalise oui and non
    def normalise_oui_non(x):
        if x in ['Oui']:
            return 'oui'

        if x in ['Non', 'Improbable', 'Non_indique']:
            return 'non'

        if x in ['Non_indique', 'non_indique', '_non_indique', 'Non_Indique', 'Non_determine_aujourdhui',
                 'nonindique', 'Non_pertinent', 'Nonindique', 'ns']:
            return np.nan

        return x

    df = df.applymap(normalise_oui_non)

    list_WH_question = ['ETABLISSEMENT_Type', 'ETABLISSEMENT_Nom', 'FORMATION_Nom',
                        'FORMATION_Domaine', 'FORMATION_Specialite', 'FORMATION_Descriptif',
                        'FORMATION_Niveau_de_diplme_lentree',
                        'FORMATION_Niveau_de_diplme_en_sortie', 'FORMATION_Duree_en_annees',
                        'FORMATION_Total_ECTS',
                        'UNITE_DE_VALEUR_COURS_Nom_du_cours',
                        'UNITE_DE_VALEUR_COURS_Notions_abordees',
                        'UNITE_DE_VALEUR_COURS_Cours_optionnel_ou_obligatoire',
                        'UNITE_DE_VALEUR_COURS_Nombre_de_credits_ECTS_accordes_par_ce_cours',
                        'UNITE_DE_VALEUR_COURS_Duree_du_cours_en_nombre_dheures',
                        'UNITE_DE_VALEUR_COURS_Mode_devaluation',
                        'UNITE_DE_VALEUR_COURS_Avis_critique_sur_le_cours_et_ou_la_formation',
                        'UNITE_DE_VALEUR_COURS_Formation_initiale_ou_continue']
    # list des questions ou 'non' n'est pas une reponse recevable et est remplacée par np.nan

    for column in list_WH_question:
        df.loc[df[column] == 'non', column] = np.nan

    list_column_drop = list(df.columns[df.count() / df.shape[0] < 0.33])
    for column in list_column_drop:
        df = df.drop(column, axis=1)

    writer = pd.ExcelWriter('./data/full_clean.xlsx')
    df.to_excel(writer, 'Recensement', index=False)
    writer.save()

    df.to_csv('./data/full_clean.csv', index=False, sep=';')

if __name__ == '__main__':
    clean_csv(csv_path='./data/full.csv')