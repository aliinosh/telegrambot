import uuid
from datetime import datetime


def generate_id():
    return str(uuid.uuid4())


def now():
    return datetime.utcnow()
