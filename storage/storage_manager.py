import os
from datetime import datetime


BASE_DIR = "storage"

IMAGES_DIR = os.path.join(BASE_DIR, "images")
PRESENTATIONS_DIR = os.path.join(BASE_DIR, "presentations")
ASSIGNMENTS_DIR = os.path.join(BASE_DIR, "assignments")


def init_storage():
    """
    Barcha storage papkalarini yaratadi
    """

    folders = [

        BASE_DIR,
        IMAGES_DIR,
        PRESENTATIONS_DIR,
        ASSIGNMENTS_DIR

    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def generate_filename(prefix, extension):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{prefix}_{timestamp}.{extension}"


def get_presentation_path():

    filename = generate_filename("presentation", "pptx")

    return os.path.join(PRESENTATIONS_DIR, filename)


def get_image_path():

    filename = generate_filename("image", "png")

    return os.path.join(IMAGES_DIR, filename)


def get_assignment_path():

    filename = generate_filename("assignment", "txt")

    return os.path.join(ASSIGNMENTS_DIR, filename)
