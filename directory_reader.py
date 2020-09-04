from os import listdir
from os.path import isdir
import sys


class DirectoryReader:
    def __init__(self, path):
        self.path = path

    def get_sequence_files(self):
        # Check if directory exists
        if not(isdir(self.path)):
            sys.exit(f"Directory '{self.path}' does not exist.")

        # Return list of directory entries sorted with path prefix
        return [f'{self.path}/{name}' for name in sorted(listdir(self.path))]
