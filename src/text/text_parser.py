from ..base_parser import BaseParser


class TextParser(BaseParser):
    def parse(self, path):
        # Process text file
        pass


def is_text_file(file_extension):
    return file_extension.lower() in ['.txt', '.html', '.xml', '.json', '.md', '.rst', '.tex', '.odt',
                                      '.docx', '.doc', '.epub', '.fb2', '.djvu', '.rtf', '.pdf']


def get_text_parser(file_extension, temp_folder_path):
    return TextParser(file_extension, temp_folder_path)
