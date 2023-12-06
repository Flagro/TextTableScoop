from ..base_parser import BaseParser


class ArchiveParser(BaseParser):
    def parse(self, path):
        # Extract archive and process its contents
        pass

    def is_archive(self):
        return True


def is_archive_file(file_extension):
    return file_extension.lower() in ['.zip', '.rar', '.7z']


def get_archive_parser(file_extension, temp_folder_path):
    return ArchiveParser(file_extension, temp_folder_path)
