from .txt_parser import TXTParser
from .html_parser import HTMLParser


def is_text_file(file_extension):
    return file_extension.lower() in ['txt', 'html', 'xml', 'json', 'md', 'rst', 'tex', 'odt',
                                      'docx', 'doc', 'epub', 'fb2', 'djvu', 'rtf', 'pdf']


def get_text_parser(file_extension, temp_folder_path):
    if file_extension.lower() in ['txt']:
        return TXTParser(file_extension, temp_folder_path)
    elif file_extension.lower() in ['html', 'xml', 'json', 'md', 'rst', 'tex', 'odt']:
        return HTMLParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported text format: {}".format(file_extension))
