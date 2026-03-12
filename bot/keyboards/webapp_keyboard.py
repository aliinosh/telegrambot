from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from aiogram.types import WebAppInfo


def webapp_keyboard():

    keyboard = [

        [
            KeyboardButton(
                text="🌐 Open Web App",
                web_app=WebAppInfo(url="https://your-webapp-url")
            )
        ]

    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
