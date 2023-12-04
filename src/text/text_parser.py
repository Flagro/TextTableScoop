from ..base_parser import BaseParser


def is_text_file(file_extension):
    return file_extension.lower() in ['.txt', '.html', '.xml', '.json', '.md', '.rst', '.tex', '.odt',
                                      '.docx', '.doc', '.epub', '.fb2', '.djvu', '.rtf', '.pdf']


class TextParser(BaseParser):
    def parse(self, path):
        # Process text file
        pass
