from .parsers.csv_parser import CSVParser


def is_table_file(file_extension):
    return file_extension.lower() in ['csv', 'xls', 'xlsx', 'xlsb', 'xlsm']


def get_table_parser(file_extension, temp_folder_path):
    if file_extension.lower() in ['csv']:
        return CSVParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported table format: {}".format(file_extension))
