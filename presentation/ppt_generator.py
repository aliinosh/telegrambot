import os

from presentation.template_manager import create_presentation
from presentation.slide_builder import build_slide
from storage.storage_manager import get_presentation_path

OUTPUT_FOLDER = "storage/presentations"


def generate_presentation(slides):

    prs = create_presentation()

    for slide in slides:

        title = slide.get("title")

        points = slide.get("points", [])

        build_slide(prs, title, points)

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    path = f"{OUTPUT_FOLDER}/presentation.pptx"

    prs.save(path)

    return path
