from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.db import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    telegram_id = Column(String, unique=True)

    language = Column(String, default="uz")

    created_at = Column(DateTime, default=datetime.utcnow)


class Presentation(Base):

    __tablename__ = "presentations"

    id = Column(Integer, primary_key=True)

    user_id = Column(String)

    topic = Column(String)

    file_path = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)


class Assignment(Base):

    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)

    user_id = Column(String)

    topic = Column(String)

    file_path = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
