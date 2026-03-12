from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def language_keyboard():

    keyboard = [

        [
            KeyboardButton(text="🇺🇿 O'zbek"),
            KeyboardButton(text="🇷🇺 Русский"),
            KeyboardButton(text="🇬🇧 English")
        ]

    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
