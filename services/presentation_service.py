from services.ai_service import generate_presentation_content
from presentation.ppt_generator import generate_presentation


def create_presentation(topic, slide_count, with_images=False):

    slides, images = generate_presentation_content(
        topic,
        slide_count,
        with_images
    )

    path = generate_presentation(
        slides,
        images
    )

    return path
