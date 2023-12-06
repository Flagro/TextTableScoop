def is_archive_file(file_extension):
    return file_extension.lower() in ['zip', 'rar', '7z']


def get_archive_parser(file_extension, temp_folder_path):
    return None
