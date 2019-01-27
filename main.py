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
header = get_header(csv_dir)

make_csv(excel_dir, csv_dir)
merge_csv(csv_dir, merged_csv_path, header=header)
clean_csv(merged_csv_path, cleaned_csv_path, cleaned_xlsx_path)
get_info(cleaned_csv_path=cleaned_csv_path)
