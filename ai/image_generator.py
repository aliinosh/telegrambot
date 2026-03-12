from ai.gemini_client import ask_gemini


def generate_image_prompt(topic, slide_title):

    prompt = f"""
    Create an image prompt for a presentation slide.

    Topic: {topic}

    Slide: {slide_title}

    Style: modern infographic
    """

    return ask_gemini(prompt)
