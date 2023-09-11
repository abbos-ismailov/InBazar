from loader import dp, db
from aiogram import types
from keyboards.inline.buy_btn_inline import rem_btn
from keyboards.default.korzinka_btn import pay_btn
 
@dp.message_handler(text="Korzinka", state=None)
async def show_purchases(msg: types.Message):
    user_purchases = await db.show_purchases(msg.from_user.id)

    for i in user_purchases:
        purchase_price = await db.get_one_clothes(int(i['product_id']))
        product_price = purchase_price['product_price'] * i['product_count']

        if i['product_count'] <= 0:
            await db.delete_product_from_korzinka(i['product_id'], msg.from_user.id)

        text = f"{i['product_name'].title()}   <b>{i['product_size']}</b> \nSoni: <b>{i['product_count']} ta</b>\n"
        text += f"Narxi: <b>{product_price}</b>"
        await msg.answer_photo(i.get("product_url"), caption=text, reply_markup=rem_btn(i['product_id']))
    await msg.answer("To'lov qilishingiz mumkin", reply_markup=pay_btn)

# BU joyda inline_btn boyicha ish qildik
@dp.callback_query_handler(lambda c: c.data.startswith("remove_from_korzinka"))
async def remove_korzinka(call: types.CallbackQuery):
    purchase_product = await db.get_one_purchases(int(call.data.split("=")[1]), call.from_user.id)
    try:
        purchase_product_count = purchase_product['product_count'] - 1
        await db.update_purchases_count(purchase_product_count, purchase_product['product_id'], call.from_user.id)
        
        # ### Update qilingandan keyingi holatini chiqaryapmiz
        new_purchase_pr = await db.get_one_purchases(purchase_product['product_id'], call.from_user.id)
        old_purchase_pr_price = await db.get_one_clothes(purchase_product['product_id'])
        
        if new_purchase_pr['product_count'] > 0:
            text = f"{new_purchase_pr['product_name'].title()}   <b>{new_purchase_pr['product_size']}</b>\n"
            text += f"Soni: {new_purchase_pr['product_count']} \n"

            pr_price = new_purchase_pr['product_count'] * old_purchase_pr_price['product_price']
            text += f"Narxi: {pr_price}"
            await call.message.answer_photo(new_purchase_pr['product_url'], caption=text)
            
            
        ### ochirishni bosganda clothesga qoshish
        new_pr_count = old_purchase_pr_price['product_count'] + 1
        await db.update_clothes_count(new_pr_count, purchase_product['product_id'])
    except Exception as e:
        print(e, "Xato...............")
        await call.message.reply("Bu mahsulotdan yoq <b>Korzinkada</b>")