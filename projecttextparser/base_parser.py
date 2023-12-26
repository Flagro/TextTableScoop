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


class TableParser(BaseParser):
    def parse(self, path):
        df = self.get_dataframes(path)

        result_dict = {
            'type': 'table',
            'csv_text': df.to_csv(),
        }
        return result_dict

    @abstractmethod
    def get_dataframes(self, path):
        # Process table file (e.g., CSV, Excel) and return a list of dicts {"dataframe": pd.DataFrame, "metadata": dict"}
        pass


class ArchiveParser(BaseParser):
    def parse(self, path):
        # Extract archive and process its contents
        pass

    def is_archive(self):
        return True
