from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

pay_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy Menyu"),
            KeyboardButton(text="To'lov qilish")
        ]
    ],
    resize_keyboard=True
)
