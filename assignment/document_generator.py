from utils.file_manager import save_text


def generate_document(topic, text):

    path = f"storage/assignments/{topic}.txt"

    save_text(path, text)

    return path
