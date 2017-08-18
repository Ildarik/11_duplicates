import os
from sys import argv

if __name__ == '__main__':
    path = argv[1]
    all_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            all_files.append([file, "/".join((root, file))])

    for item in sorted(all_files):
        print(item)