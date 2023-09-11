from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

clothes_size = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="S"),
            KeyboardButton(text="M"),
            KeyboardButton(text="L")
        ],
        [
            KeyboardButton(text="XL"),
            KeyboardButton(text="XXL"),
            KeyboardButton(text="XXXL")
        ]
    ],
    resize_keyboard=True
)

clothes_name = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="futbolka"),
            KeyboardButton(text="bosh kiyim")
        ],
        [
            KeyboardButton(text="kurtka"),
            KeyboardButton(text="sharf"),
        ],
        [
            KeyboardButton(text="jacket"),
            KeyboardButton(text="shim"),  
        ],
        [
            KeyboardButton(text="shortik"),
            KeyboardButton(text="ishton"),   
        ],
        [
            KeyboardButton(text="tufli"),
            KeyboardButton(text="krosovka"),
        ],
        [
            KeyboardButton(text="boshqa kiyimlar"),
            KeyboardButton(text="Asosiy Menyu")
        ]
    ],
    resize_keyboard=True
)