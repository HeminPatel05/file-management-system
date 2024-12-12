import os
import hashlib
from .utils.logger import Logger

class DuplicateHandler:
    def __init__(self, directory):
        self.directory = directory
        self.logger = Logger()
        self.hash_dict = {}

    def get_file_hash(self, filepath):
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def find_duplicates(self):
        duplicates = []
        for root, _, files in os.walk(self.directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = self.get_file_hash(filepath)
                if file_hash in self.hash_dict:
                    duplicates.append((filepath, self.hash_dict[file_hash]))
                else:
                    self.hash_dict[file_hash] = filepath
        return duplicates
