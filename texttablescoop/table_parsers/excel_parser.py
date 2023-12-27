from xlsx2pandas import get_df

from ..base_parser import TableParser


class ExcelParser(TableParser):
    def get_dataframes(self, path):
        output = get_df(path, prettify_output=False)
        result = []
        for sheet_name, dfs in output.items():
            for df in dfs:
                result.append((df, {'sheet_name': sheet_name}))
        return result
