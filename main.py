from excel_manager import make_csv
from csv_merging import merge_csv
from csv_cleaning import clean_csv
from get_info import get_info
from get_header import get_header

excel_dir = './data/excel/'
csv_dir = './data/csv/'
merged_csv_path = "./data/merged.csv"
cleaned_csv_path = './data/cleaned.csv'
cleaned_xlsx_path = './data/cleaned.xlsx'

header = ['ETABLISSEMENT_Type',
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

make_csv(excel_dir, csv_dir)
merge_csv(csv_dir, merged_csv_path, header=header)
clean_csv(merged_csv_path, cleaned_csv_path, cleaned_xlsx_path)
get_info(cleaned_csv_path=cleaned_csv_path)
