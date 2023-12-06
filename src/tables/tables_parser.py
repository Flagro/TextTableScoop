from abc import abstractmethod

from ..base_parser import BaseParser
from .parsers.csv_parser import CSVParser


class TableParser(BaseParser):
    def parse(self, path):
        df = self.get_pandas_dataframe(path)
        result_dict = {
            'type': 'table',
            'csv_text': df.to_csv(),
        }
        return result_dict

    @abstractmethod
    def get_pandas_dataframe(self, path):
        # Process table file (e.g., CSV, Excel)
        pass


def is_table_file(file_extension):
    return file_extension.lower() in ['.csv', '.xls', '.xlsx', 'xlsb', 'xlsm']


def get_table_parser(file_extension, temp_folder_path):
    if file_extension.lower() in ['.csv']:
        return CSVParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported table format: {}".format(file_extension))
