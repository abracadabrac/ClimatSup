import pandas as pd

# [Nom, Type, Env, Clim, option]

def get_info(cleaned_csv_path):
    print(" ")
    df = pd.read_csv(cleaned_csv_path, sep=';')

    list_Nom_formation_total = df.FORMATION_Nom.unique()
    list_Nom_formation_ENV = df[
        df.UNITE_DE_VALEUR_COURS_Questions_ENV_au_sens_large_evoquees_oui_non == 'oui'].FORMATION_Nom.unique()
    list_Nom_formation_TRANS = df[
        df.UNITE_DE_VALEUR_COURS_Enjeux_transition_energetiqueclimat_abordes_oui_non == 'oui'].FORMATION_Nom.unique()

    print("proportion de formations traitant d'environement",
          len(list_Nom_formation_ENV) / len(list_Nom_formation_total), '\n')
    print("proportion de formations traitant de transition",
          len(list_Nom_formation_TRANS) / len(list_Nom_formation_total), '\n')

    dict_type_fomation_total = dict(df.groupby('ETABLISSEMENT_Type').FORMATION_Nom.unique())
    dict_type_formation_ENV = dict(
        df[df.UNITE_DE_VALEUR_COURS_Questions_ENV_au_sens_large_evoquees_oui_non == 'oui'].groupby(
            'ETABLISSEMENT_Type').FORMATION_Nom.unique())
    dict_type_formation_TRANS = dict(
        df[df.UNITE_DE_VALEUR_COURS_Enjeux_transition_energetiqueclimat_abordes_oui_non == 'oui'].groupby(
            'ETABLISSEMENT_Type').FORMATION_Nom.unique())

    dict_formarion_ratio_ENV = {formation_type: len(list_formation_ENV) / len(list_formation_total) for
                                (formation_type, list_formation_ENV), (formation_type, list_formation_total)
                                in zip(dict_type_formation_ENV.items(), dict_type_fomation_total.items())}
    dict_formarion_ratio_TRANS = {formation_type: len(list_formation_TRANS) / len(list_formation_total) for
                                (formation_type, list_formation_TRANS), (formation_type, list_formation_total)
                                in zip(dict_type_formation_TRANS.items(), dict_type_fomation_total.items())}

    print("proportion de formation traitant d'environement par type de formation \n", dict_formarion_ratio_ENV, '\n')
    print("proportion de formation traitant de transition par type de formation \n", dict_formarion_ratio_TRANS, '\n')

    dict_ecole_formation_total = dict(df.groupby('ETABLISSEMENT_Nom').FORMATION_Nom.unique())

    dict_ecole_formation_ENV = dict(
        df[df.UNITE_DE_VALEUR_COURS_Questions_ENV_au_sens_large_evoquees_oui_non == 'oui'].groupby(
            'ETABLISSEMENT_Nom').FORMATION_Nom.unique())

    dict_ecole_formation_TRANS = dict(
        df[df.UNITE_DE_VALEUR_COURS_Enjeux_transition_energetiqueclimat_abordes_oui_non == 'oui'].groupby(
            'ETABLISSEMENT_Nom').FORMATION_Nom.unique())

    dict_ecole_ratio_ENV = {ecole: len(list_formation_ENV) / len(list_formation_total) for
                            (ecole, list_formation_ENV), (ecole, list_formation_total)
                            in zip(dict_ecole_formation_ENV.items(), dict_ecole_formation_total.items())}

    dict_ecole_ratio_TRANS = {ecole: len(list_formation_TRANS) / len(list_formation_total) for
                              (ecole, list_formation_TRANS), (ecole, list_formation_total)
                              in zip(dict_ecole_formation_TRANS.items(), dict_ecole_formation_total.items())}

    print("proportion de formation traitant d'environement par ecole de formation \n", dict_ecole_ratio_ENV, '\n')
    print("proportion de formation traitant de transition par ecole de formation \n", dict_ecole_ratio_TRANS, '\n')


if __name__ == '__main__':
    cleaned_csv_path = './data/cleaned.csv'
    get_info(cleaned_csv_path)


