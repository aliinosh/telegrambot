from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.language_keyboard import language_keyboard

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await message.answer(
        "Tilni tanlang / Choose language",
        reply_markup=language_keyboard()
    )
