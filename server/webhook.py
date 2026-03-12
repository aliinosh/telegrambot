from aiogram import Router
from aiogram.types import Message, WebAppData

from services.presentation_service import create_presentation

router = Router()


@router.message(lambda m: m.web_app_data)
async def webapp_data(message: Message):

    import json

    data = json.loads(message.web_app_data.data)

    topic = data["topic"]

    slides = int(data["slides"])

    images = data["images"]

    path = create_presentation(
        topic,
        slides,
        images
    )

    await message.answer_document(
        document=open(path, "rb")
    )
