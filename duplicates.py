import os
from collections import defaultdict
from sys import argv


def get_files_dict(path_dir):
    result_dict = defaultdict(list)
    for root, dirs, files in os.walk(path_dir):
        for file_name in files:
            full_file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(full_file_path)
            result_dict[(file_name, file_size)].append(full_file_path)
    return result_dict

def get_duplicated_files_dict(files_dict):
    return {key: value for key, value in files_dict.items() if len(value) > 1}


if __name__ == '__main__':
    path_dir = argv[1]
    files_dict = get_files_dict(path_dir)