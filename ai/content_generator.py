from ai.gemini_client import ask_gemini


def generate_slides(topic):

    prompt = f"""
    {topic} haqida PowerPoint taqdimot yoz.

    8 ta slayd yarat.

    Format:

    Slide title:
    Bullet points:
    """

    text = ask_gemini(prompt)

    return text
