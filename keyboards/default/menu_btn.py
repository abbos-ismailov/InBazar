from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_choice_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kiyimlar"),
            KeyboardButton(text="Korzinka"),
            KeyboardButton(text="Dogs")
        ]
    ],
    resize_keyboard=True
)