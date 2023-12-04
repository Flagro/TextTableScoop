from ..base_parser import BaseParser


def is_table_file(file_extension):
    return file_extension.lower() in ['.csv', '.xls', '.xlsx', 'xlsb', 'xlsm']


class TableParser(BaseParser):
    def parse(self, path):
        # Process table file (e.g., CSV, Excel)
        pass
