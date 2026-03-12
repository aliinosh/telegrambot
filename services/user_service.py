users = {}


def create_user(user_id):

    if user_id not in users:

        users[user_id] = {
            "language": "uz"
        }


def set_language(user_id, language):

    if user_id in users:

        users[user_id]["language"] = language


def get_language(user_id):

    if user_id in users:
        return users[user_id]["language"]

    return "uz"
