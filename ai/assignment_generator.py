from ai.gemini_client import ask_gemini


def generate_assignment(topic, pages=3):

    prompt = f"""
    Write an academic assignment.

    Topic: {topic}

    Pages: {pages}

    Structure:

    Introduction
    Main part
    Conclusion
    References
    """

    return ask_gemini(prompt)
