from ..base_parser import TextParser


class HTMLParser(TextParser):
    def get_text(self, path):
        with open(path, 'r') as file:
            # Read the file content
            content = file.read()
        return content
