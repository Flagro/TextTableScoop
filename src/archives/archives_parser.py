from ..base_parser import BaseParser


def is_archive_file(file_extension):
    return file_extension.lower() in ['.zip', '.rar', '.7z']


class ArchiveParser(BaseParser):
    def parse(self, path):
        # Extract archive and process its contents
        pass

    def is_archive(self):
        return True
