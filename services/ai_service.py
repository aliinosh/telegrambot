from ai.slide_planner import create_slide_plan
from ai.text_generator import generate_slide_text
from ai.image_generator import generate_image_prompt


def generate_presentation_content(topic, slide_count, with_images=False):

    slides = []

    slide_titles = create_slide_plan(topic, slide_count)

    images = []

    for title in slide_titles:

        points = generate_slide_text(topic, title)

        slide = {
            "title": title,
            "points": points
        }

        slides.append(slide)

        if with_images:
            img_prompt = generate_image_prompt(topic, title)
            images.append(img_prompt)

    return slides, images
