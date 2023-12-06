from ..text_parser import TextParser

class HTMLParser(TextParser):
    def parse(self, path):
        with open(path, 'r') as file:
            # Read the file content
            content = file.read()
        return content
