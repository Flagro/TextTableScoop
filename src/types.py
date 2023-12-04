from .archives.archives_parser import is_archive_file, ArchiveParser
from .tables.tables_parser import is_table_file, TableParser
from .text.text_parser import is_text_file, TextParser


def get_file_parser(file_extension, temp_folder_path):
    if is_archive_file(file_extension):
        return ArchiveParser(file_extension, temp_folder_path)
    elif is_table_file(file_extension):
        return TableParser(file_extension, temp_folder_path)
    elif is_text_file(file_extension):
        return TextParser(file_extension, temp_folder_path)
    else:
        raise Exception("Unsupported file format: {}".format(file_extension))
