import xlrd
import csv
import os


def csv_from_excel(xl_file, csv_dir):
    """
    Je ne peux pas travailler directement sur des fichiers excel, je les converti en format csv.

    :param xl_file: fichier excel ex: 'data/excel/ecole_des_mines.exls'
    :return:
    """
    # recuperation du nom de l'ecole pour donner comme nom au fichier csv
    base = os.path.basename(xl_file)
    name = os.path.splitext(base)[0].encode("utf8")

    # ouverture du fichier excel et lecture du bonne onglet
    wb = xlrd.open_workbook(xl_file)

    unconsidered_sheets = ['Consignes', 'Exemples', 'Listes']       # list des onglets inutiles

    # creation du csv et recopie du excel
    with open('%s%s.csv' % (csv_dir, name), 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)

        for sheet_name in wb.sheet_names():
            if sheet_name not in unconsidered_sheets:
                sh = wb.sheet_by_name(sheet_name)
                for nb_row in range(sh.nrows):
                    row = sh.row_values(nb_row)
                    wr.writerow(row)


def make_csv(excel_dir, csv_dir):

    list_file = os.listdir(excel_dir)
    for file in list_file:
        print(file)
        csv_from_excel(excel_dir + file, csv_dir)
