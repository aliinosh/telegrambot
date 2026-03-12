from aiogram import Router
from aiogram.types import Message
from services.assignment_service import create_assignment

router = Router()


@router.message(lambda m: m.text == "📄 Assignment")
async def assignment(message: Message):

    await message.answer("Send assignment topic")


@router.message()
async def generate_assignment(message: Message):

    topic = message.text

    path = create_assignment(topic, 3)

    await message.answer_document(
        document=open(path, "rb")
    )
