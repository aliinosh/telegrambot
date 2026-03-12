from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.keyboards.main_menu_keyboard import main_menu_keyboard
from services.user_service import set_language

router = Router()


@router.message(lambda m: m.text in ["🇺🇿 O'zbek", "🇷🇺 Русский", "🇬🇧 English"])
async def set_user_language(message: Message, state: FSMContext):

    user_id = message.from_user.id

    if "O'zbek" in message.text:
        lang = "uz"

    elif "Русский" in message.text:
        lang = "ru"

    else:
        lang = "en"

    set_language(user_id, lang)

    await message.answer(
        "Language saved",
        reply_markup=main_menu_keyboard()
    )

    await state.clear()
