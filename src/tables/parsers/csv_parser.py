from ..tables_parser import TableParser

class CSVParser(TableParser):
    def parse(self, path):
        with open(path, 'r') as file:
            # Read the file content
            content = file.read()
        return content
