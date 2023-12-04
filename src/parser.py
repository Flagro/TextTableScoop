from .utils import iterate_directory_files, is_dir, get_parent_folder
from .types import get_file_parser


class JSONOutputCollector:
    def __init__(self):
        self._output = []

    def add(self, file_path, **kwargs):
        entry = {
            "file_path": file_path,
            "params": kwargs
        }
        self._output.append(entry)

    def get(self):
        return self._output


class ProjectTraverser:
    def __init__(self, ignore_patterns, temp_folder_path, json_output_collector):
        self._ignore_patterns = ignore_patterns
        self._temp_folder_path = temp_folder_path
        self._json_output_collector = json_output_collector

    def process_directory(self, path, relative_path):
        for file_path, new_relative_path in iterate_directory_files(path, self._ignore_patterns, relative_path):
            self.process_file(file_path, new_relative_path)

    def process_file(self, file_path, relative_path):
        file_parser = get_file_parser(file_path, relative_path)
        if file_parser.is_archive():
            self.process_archive(file_parser, relative_path)
        else:
            self._json_output_collector.add(relative_path, file_parser.parse())

    def process_archive(self, file_parser, relative_path):
        with file_parser.parse() as unpacked_folder_path:
            self.process_directory(unpacked_folder_path, relative_path)


def process(path, temp, project, ignore):
    ignore_patterns = [pattern.strip() for pattern in ignore.split(',')] if ignore else []
    json_output_collector = JSONOutputCollector()
    project_traverser = ProjectTraverser(ignore_patterns, temp, json_output_collector)
    if project is None:
        project = get_parent_folder(path)
    if is_dir(path):
        project_traverser.process_directory(path, "")
    else:
        project_traverser.process_file(path, project)
    return json_output_collector.get()
