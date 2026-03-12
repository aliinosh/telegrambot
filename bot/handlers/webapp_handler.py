from aiogram import Router
from aiogram.types import Message

from bot.keyboards.webapp_keyboard import webapp_keyboard

router = Router()


@router.message(lambda m: m.text == "🌐 Web App")
async def open_webapp(message: Message):

    await message.answer(
        "Open presentation creator:",
        reply_markup=webapp_keyboard()
    )
