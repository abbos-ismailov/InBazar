from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buy_product(count, id):
    buy_btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="-", callback_data="product_minus"),
                InlineKeyboardButton(text=count, callback_data="product_value"),
                InlineKeyboardButton(text="+", callback_data="product_plus")
            ],
            # [
            #     InlineKeyboardButton(text="buy", callback_data=)
            # ]
        ]
    )
    return buy_btn
    
def rem_btn(pr_id):
    a = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="remove", callback_data=f"remove_from_korzinka={pr_id}")
            ]
        ]
    )
    return a