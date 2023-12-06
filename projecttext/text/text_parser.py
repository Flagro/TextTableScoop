from abc import abstractmethod

from ..base_parser import BaseParser
from .parsers.txt_parser import TXTParser
from .parsers.html_parser import HTMLParser


class TextParser(BaseParser):
    def parse(self, path):
        text = self.get_text(path)
        result_dict = {
            'type': 'text',
            'text': text,
        }
        return result_dict

    @abstractmethod
    def get_text(self, path):
        # Get text from text file
        pass


def is_text_file(file_extension):
    return file_extension.lower() in ['.txt', '.html', '.xml', '.json', '.md', '.rst', '.tex', '.odt',
                                      '.docx', '.doc', '.epub', '.fb2', '.djvu', '.rtf', '.pdf']


def get_text_parser(file_extension, temp_folder_path):
    if file_extension.lower() in ['.txt']:
        return TXTParser(file_extension, temp_folder_path)
    elif file_extension.lower() in ['.html', '.xml', '.json', '.md', '.rst', '.tex', '.odt']:
        return HTMLParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported text format: {}".format(file_extension))
