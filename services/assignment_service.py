from ai.assignment_generator import generate_assignment


def create_assignment(topic, pages):

    text = generate_assignment(topic, pages)

    file_path = f"storage/assignments/{topic}.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    return file_path
