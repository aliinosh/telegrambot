from ai.gemini_client import ask_gemini


def create_slide_plan(topic, slide_count):

    prompt = f"""
    Create a presentation outline about: {topic}

    Slides: {slide_count}

    Return format:

    Slide 1: title
    Slide 2: title
    """

    result = ask_gemini(prompt)

    slides = []

    for line in result.split("\n"):

        if "Slide" in line:

            title = line.split(":")[-1].strip()

            slides.append(title)

    return slides
