from abc import abstractmethod
import os

class ParsebleFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.is_lockable = False
        self.office_format = False


class ProjectParser:
    @abstractmethod
    def __init__(self, tmp_folder_path):
        self.tmp_folder_path = tmp_folder_path

    @abstractmethod
    def parse(self, path):
        pass

class FolderToFilesParser:
    def __init__(self, tmp_folder_path):
        self.tmp_folder_path = tmp_folder_path

    def parse(self, path):
        pass

class FileToTextParser:
    def __init__(self, tmp_folder_path):
        self.tmp_folder_path = tmp_folder_path

    def parse(self, path):
        pass

def process():
    pass
