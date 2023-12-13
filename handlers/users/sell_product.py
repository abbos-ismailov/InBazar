from loader import dp, db
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.default.menu_btn import menu_choice_btn
from keyboards.default.product_btn import clothes_name
from keyboards.inline.buy_btn_inline import buy_btn

@dp.message_handler(text="Asosiy Menyu")
async def main_menu(msg: types.Message):
    await msg.answer("Kiyimlar yoki Korzinka bo'limini tanlashingiz mumkin", reply_markup=menu_choice_btn)

@dp.message_handler(Command("menu"))
async def menu(msg: types.Message):
    await msg.answer("Xarid qilish uchun kiyimlar bo'limini tanlashiz mumkin", reply_markup=menu_choice_btn)

@dp.message_handler(text="Kiyimlar", state=None)
async def kiyimlar(msg: types.Message):
    await msg.answer("Kiyimlar turini tanlang", reply_markup=clothes_name)

### Kiyim nomini tashlaganda shu kiyimni foydalanuvchiga chiqarib beryapmiz
@dp.message_handler(text="futbolka", state=None)
async def out_t_shirt(msg: types.Message):
    products = await db.select_product("futbolka")
    index = 0
    active_product = products[index]
    # for i in products:
    #     product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
    #     product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
    #     product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
    #     await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

    product_caption = f"NOMI=<b>{active_product.get('product_name')}</b>\nRAZMER=<b>{active_product.get('product_size')}</b>\n"
    product_caption += f"ID=<b>{active_product.get('product_id')}</b>\nSONI=<b>{active_product.get('product_count')}</b>\n"
    product_caption += f"NARXI=<b>{active_product.get('product_price')}</b>"
    await msg.answer_photo(active_product["product_url"], caption=product_caption, reply_markup=buy_btn)
    
@dp.message_handler(text="bosh kiyim", state=None)
async def out_headdress(msg: types.Message):
    products = await db.select_product("bosh kiyim")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="kurtka", state=None)
async def out_kurtka(msg: types.Message):
    products = await db.select_product("kurtka")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="sharf", state=None)
async def out_scarf(msg: types.Message):
    products = await db.select_product("sharf")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="jacket", state=None)
async def out_jacket(msg: types.Message):
    products = await db.select_product("jacket")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="shim", state=None)
async def out_trausers(msg: types.Message):
    products = await db.select_product("shim")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="shortik", state=None)
async def out_shortik(msg: types.Message):
    products = await db.select_product("shortik")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="ishton", state=None)
async def out_ishton(msg: types.Message):
    products = await db.select_product("ishton")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="tufli", state=None)
async def out_tufli(msg: types.Message):
    products = await db.select_product("tufli")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="krosovka", state=None)
async def out_krosovka(msg: types.Message):
    products = await db.select_product("krosovka")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)

@dp.message_handler(text="boshqa kiyimlar", state=None)
async def out_others_dress(msg: types.Message):
    products = await db.select_product("boshqa kiyimlar")
    for i in products:
        product_caption = f"NOMI=<b>{i.get('product_name')}</b>\nRAZMER=<b>{i.get('product_size')}</b>\n"
        product_caption += f"ID=<b>{i.get('product_id')}</b>\nSONI=<b>{i.get('product_count')}</b>\n"
        product_caption += f"NARXI=<b>{i.get('product_price')}</b>"
        await msg.answer_photo(i["product_url"], caption=product_caption, reply_markup=buy_btn)



### Sotib olishni bosganda purchases Tablega yozdik
@dp.callback_query_handler(text="buy_btn_click")
async def put_backet(call: types.CallbackQuery):
    item_list = call.message.caption.split("\n")
    new_elem_list = []
    for i in item_list:
        x = i.split("=")
        new_elem_list.append(x)
    
    purchase_item_count = 1
    purchase_item = await db.get_from_purchases(product_id=int(new_elem_list[2][1]), user_tg_id=call.from_user.id)
    clothes_item = await db.get_one_clothes(int(new_elem_list[2][1]))
    print(purchase_item)
    
    if purchase_item != None:
        purchase_item_count = purchase_item.get('product_count')
        purchase_item_count += 1
        await db.update_purchases_count(purchase_item_count, int(new_elem_list[2][1]), user_tg_id=call.from_user.id)
        
        clothes_item_count = clothes_item.get('product_count')
        clothes_item_count -= 1
        await db.update_clothes_count(clothes_item_count, int(new_elem_list[2][1]))
    else:
        await db.add_to_korzinka(call.from_user.id, int(new_elem_list[2][1]), call.message.photo[-1].file_id, new_elem_list[1][1], new_elem_list[0][1], purchase_item_count)

        clothes_item_count = clothes_item.get('product_count')
        clothes_item_count -= 1
        await db.update_clothes_count(clothes_item_count, int(new_elem_list[2][1]))
    
    
    await call.answer("Korzinkaga tushdi") 

    text = "Siz shu kiyimni sotib oldingiz\nAgar ochirmoqchi bolsangiz <b>Korzinka</b> bolimidan ochirasiz"
    await call.message.reply(text)