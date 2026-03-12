from ai.gemini_client import ask_gemini
from storage.storage_manager import get_image_path
path = get_image_path()

with open(path, "wb") as f:
    f.write(image_bytes)
def generate_image_prompt(topic, slide_title):

    prompt = f"""
    Create an image prompt for a presentation slide.

    Topic: {topic}

    Slide: {slide_title}

    Style: modern infographic
    """

    return ask_gemini(prompt)
