import os


def ensure_folder(path):

    if not os.path.exists(path):
        os.makedirs(path)


def save_text(path, text):

    ensure_folder(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_file(path):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
