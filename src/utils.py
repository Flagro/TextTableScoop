import os
import fnmatch


def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]


def get_file_name(file_path):
    return os.path.basename(file_path)


def should_ignore(path, ignore_patterns):
    return any(fnmatch.fnmatch(path, pattern) for pattern in ignore_patterns)


def iterate_directory_files(path, ignore_patterns, parent_folder_path):
    for dirpath, dirnames, filenames in os.walk(path):
        # Filter directories and files based on ignore patterns
        dirnames[:] = [d for d in dirnames if not should_ignore(os.path.join(dirpath, d), ignore_patterns)]
        filenames[:] = [f for f in filenames if not should_ignore(os.path.join(dirpath, f), ignore_patterns)]

        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(full_path, start=path)
            yield (full_path, os.path.join(parent_folder_path, relative_path))


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)
