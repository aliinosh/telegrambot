from database.models import User, Presentation, Assignment
from database.db import SessionLocal


def create_user(telegram_id):

    db = SessionLocal()

    user = User(telegram_id=telegram_id)

    db.add(user)

    db.commit()

    db.close()


def get_user(telegram_id):

    db = SessionLocal()

    user = db.query(User).filter(
        User.telegram_id == telegram_id
    ).first()

    db.close()

    return user


def set_language(telegram_id, language):

    db = SessionLocal()

    user = db.query(User).filter(
        User.telegram_id == telegram_id
    ).first()

    if user:

        user.language = language

        db.commit()

    db.close()
