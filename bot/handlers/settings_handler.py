from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda m: m.text == "⚙ Settings")
async def settings(message: Message):

    await message.answer(
        "Settings:\n"
        "Use /start to change language"
    )
