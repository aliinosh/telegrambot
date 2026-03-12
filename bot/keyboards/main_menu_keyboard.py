from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton


def main_menu_keyboard():

    keyboard = [

        [
            KeyboardButton(text="📊 Presentation"),
            KeyboardButton(text="📄 Assignment")
        ],

        [
            KeyboardButton(text="🌐 Web App"),
            KeyboardButton(text="⚙ Settings")
        ]

    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
