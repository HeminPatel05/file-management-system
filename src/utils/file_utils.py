import os
import magic

def get_file_type(filepath):
    mime = magic.Magic()
    try:
        file_type = mime.from_file(filepath)
        return file_type
    except Exception:
        return "unknown"

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_size(filepath):
    return os.path.getsize(filepath)
