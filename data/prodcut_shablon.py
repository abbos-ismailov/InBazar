from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.tolov_shablon import Product
from loader import db
from aiogram.types import LabeledPrice

# purchases_clothes = await db.show_purchases(user_tg_id=)
async def clothes_pr(user_id):
    
    purchases_clothes = await db.show_purchases(user_tg_id=user_id)
    prices_list = [LabeledPrice(
                label=f"Kuzgi chegirma",
                amount=-20000*100
            )]
    
    for pr in purchases_clothes:
        prices_purchase_pr = await db.select_product_clothes(pr['product_id'])
        pr_price = prices_purchase_pr['product_price']
        
        pr_count = pr['product_count']
        pr_name = pr['product_name']

        price_label = LabeledPrice(
                label=f"{pr_name} => {pr_price} so'm * {pr_count} ta   =",
                amount=pr_count*pr_price*100
            )
        prices_list.append(price_label)
    

    
    

    clothes = Product(   
        title="To'lov qilish",
        description="InBazar",
        currency="UZS",
        prices=prices_list,
        start_parameter="create_invoice_clothes",
        photo_url="https://cdn2.iconfinder.com/data/icons/transports-2/200/Untitled-9-1024.png",
        photo_width=1280,
        photo_height=564,
        need_name=True,
        need_phone_number=True,
        need_shipping_address=True,
        is_flexible=True
    )
    return clothes



REGULAR_SHIPPING = types.ShippingOption(
    id='three_day',
    title="3 kunda yetkaziladi",
    prices=[
        LabeledPrice("Maxsus o'ram", 5_000_00),
        LabeledPrice("3 kunda yetkazish xizmati", 10_000_00),
    ]
)


FAST_SHIPPING = types.ShippingOption(
    id='one_day',
    title="1 kunda yetkaziladi",
    prices=[
        LabeledPrice("Maxsus o'ram", 5_000_00),
        LabeledPrice("1 kunda yetkazish xizmati", 30_000_00),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id='dokon',
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("Dastavkasiz", -10_000_00),
    ]
)