def validate_slide_count(count):

    if count < 1:
        return False

    if count > 25:
        return False

    return True
