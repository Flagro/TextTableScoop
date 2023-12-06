import pandas as pd

from ..base_parser import TableParser


class CSVParser(TableParser):
    def get_pandas_dataframe(self, path):
        df = pd.read_csv(path)
        return df
