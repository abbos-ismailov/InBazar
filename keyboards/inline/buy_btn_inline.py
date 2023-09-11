from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="buy", callback_data="buy_btn_click")
        ]
    ]
)

def rem_btn(pr_id):
    a = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="remove", callback_data=f"remove_from_korzinka={pr_id}")
            ]
        ]
    )
    return a