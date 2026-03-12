import os

def save_file(path, data):

    with open(path, "wb") as f:
        f.write(data)

def file_exists(path):
    return os.path.exists(path)
