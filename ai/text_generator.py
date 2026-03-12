from ai.gemini_client import ask_gemini


def generate_slide_text(topic, slide_title):

    prompt = f"""
    Write slide content.

    Topic: {topic}

    Slide title: {slide_title}

    Write 4 bullet points.
    """

    text = ask_gemini(prompt)

    points = []

    for line in text.split("\n"):

        line = line.replace("-", "").strip()

        if line:
            points.append(line)

    return points
