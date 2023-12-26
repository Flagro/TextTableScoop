from .csv_parser import CSVParser
from .excel_parser import ExcelParser


def is_table_file(file_extension):
    return file_extension.lower() in ['csv', 'xls', 'xlsx', 'xlsb', 'xlsm']


def get_table_parser(file_extension, temp_folder_path):
    if file_extension.lower() in ['csv']:
        return CSVParser(file_extension, temp_folder_path)
    elif file_extension.lower() in ['xlsx', 'xlsm', 'xls', 'xlsb']:
        return ExcelParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported table format: {}".format(file_extension))
