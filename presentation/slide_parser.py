def parse_slides(text):

    slides = []

    blocks = text.split("Slide")

    for block in blocks:

        if "title" in block.lower():

            lines = block.split("\n")

            title = lines[0]

            points = lines[1:]

            slides.append({
                "title": title,
                "points": points
            })

    return slides
