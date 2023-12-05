from ..base_parser import BaseParser


class TableParser(BaseParser):
    def parse(self, path):
        # Process table file (e.g., CSV, Excel)
        pass


def is_table_file(file_extension):
    return file_extension.lower() in ['.csv', '.xls', '.xlsx', 'xlsb', 'xlsm']


def get_table_parser(file_extension, temp_folder_path):
    return TableParser(file_extension, temp_folder_path)
