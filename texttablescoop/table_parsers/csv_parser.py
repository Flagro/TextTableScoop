import pandas as pd

from ..base_parser import TableParser


class CSVParser(TableParser):
    def get_dataframes(self, path):
        df = pd.read_csv(path)
        return [(df, {})]
