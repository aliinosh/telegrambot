def validate_slide_count(count):

    try:
        count = int(count)
    except:
        return False

    if count < 1 or count > 25:
        return False

    return True
