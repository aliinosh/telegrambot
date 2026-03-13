import os
from datetime import datetime

BASE_DIR = "storage"

IMAGES_DIR = os.path.join(BASE_DIR, "images")
PRESENTATIONS_DIR = os.path.join(BASE_DIR, "presentations")
ASSIGNMENTS_DIR = os.path.join(BASE_DIR, "assignments")


def init_storage():

    folders = [
        BASE_DIR,
        IMAGES_DIR,
        PRESENTATIONS_DIR,
        ASSIGNMENTS_DIR
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def generate_filename(prefix, ext):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{prefix}_{timestamp}.{ext}"


def get_image_path():
    return os.path.join(IMAGES_DIR, generate_filename("image", "png"))


def get_presentation_path():
    return os.path.join(PRESENTATIONS_DIR, generate_filename("presentation", "pptx"))


def get_assignment_path():
    return os.path.join(ASSIGNMENTS_DIR, generate_filename("assignment", "docx"))
