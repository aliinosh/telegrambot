from aiogram import Router
from aiogram.types import Message

from bot.keyboards.main_menu_keyboard import main_menu_keyboard

router = Router()


@router.message()
async def start_menu(message: Message):

    if message.text == "menu":

        await message.answer(
            "Main Menu",
            reply_markup=main_menu_keyboard()
        )
