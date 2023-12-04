from abc import ABC, abstractmethod


class BaseParser(ABC):
    def __init__(self, file_extension, temp_folder_path):
        self._file_extension = file_extension
        self._temp_folder_path = temp_folder_path

    @abstractmethod
    def parse(self, path):
        pass

    def is_archive(self):
        return False
