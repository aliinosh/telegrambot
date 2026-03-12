from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def slide_count_keyboard():

    keyboard = [

        [
            KeyboardButton(text="5"),
            KeyboardButton(text="10"),
            KeyboardButton(text="15")
        ],

        [
            KeyboardButton(text="20"),
            KeyboardButton(text="25")
        ]

    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
