from ai.gemini_client import generate

def generate_presentation_text(topic, slides):

    prompt = f"""
    Create a presentation about {topic}

    Slides: {slides}

    Each slide should contain:

    Title
    Bullet points
    """

    return generate(prompt)
