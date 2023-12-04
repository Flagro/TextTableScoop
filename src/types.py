import os

archive_formats = ['.zip', '.rar', '.7z']
table_formats = ['.csv', '.xls', '.xlsx', 'xlsb', 'xlsm']
text_formats = ['.txt', '.html', '.xml', '.json', '.md', '.rst', '.tex', '.odt', 
                '.docx', '.doc', '.epub', '.fb2', '.djvu', '.rtf', '.pdf']


def is_archive(file_path):
    return os.path.splitext(file_path)[1] in archive_formats


def is_table(file_path):
    return os.path.splitext(file_path)[1] in table_formats


def is_text(file_path):
    return os.path.splitext(file_path)[1] in text_formats
