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
        texts = self.get_texts(path)
        result = []
        for text, metadata in texts:
            result.append({
                'data_type': 'text',
                'text': text,
                'metadata': metadata
            })
        return result

    @abstractmethod
    def get_texts(self, path):
        # Get text from text file
        pass


class TableParser(BaseParser):
    def parse(self, path):
        dfs = self.get_dataframes(path)
        result = []
        for df, metadata in dfs:
            result.append({
                'data_type': 'table',
                'csv_text': df.to_csv(),
                'metadata': metadata
            })
        return result

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
