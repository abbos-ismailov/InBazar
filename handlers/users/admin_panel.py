from data.config import ADMINS
from aiogram import types
from aiogram.types import ContentType, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command
from loader import dp, db
from states.add_product_state import Add_product_states, Delete
from aiogram.dispatcher import FSMContext
from pathlib import Path
from keyboards.default.product_btn import clothes_size, clothes_name

download_path = Path().joinpath("inbazar data")
download_path.mkdir(parents=False, exist_ok=True)


@dp.message_handler(Command("add_product", prefixes="?/"), user_id=ADMINS)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nMahsulotni nomini kiriting.", reply_markup=clothes_name)
    await Add_product_states.product_name.set()

@dp.message_handler(state=Add_product_states.product_name)
async def get_product_name(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"product_name": msg.text}
    )
    await msg.answer("Mahsulot olchamini kiriting \n<b>(S, M, L, XL, XXL, XXXL)</b>", reply_markup=clothes_size)
    await Add_product_states.product_size.set()

@dp.message_handler(state=Add_product_states.product_size)
async def get_product_name(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"product_size": msg.text}
    )
    await msg.answer("Mahsulotni narxini kiriting", reply_markup=ReplyKeyboardRemove())
    await Add_product_states.product_price.set()

@dp.message_handler(state=Add_product_states.product_price)
async def get_product_name(msg: types.Message, state: FSMContext):
    price = msg.text
    price_list = price.split(" ")
    product_price = "_".join(price_list)
    await msg.answer(product_price)
    await state.update_data(
        {"product_price": product_price}
    )
    await msg.answer("Mahsulotni sonini kiriting")
    await Add_product_states.product_count.set()

@dp.message_handler(state=Add_product_states.product_count)
async def get_product_name(msg: types.Message, state: FSMContext):
    await state.update_data( 
        {"product_count": msg.text}
    )
    await msg.answer("Mahsulotni rasmini tashlang")
    await Add_product_states.product_img.set()

@dp.message_handler(state=Add_product_states.product_img, content_types=ContentType.PHOTO)
async def get_product_img(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"product_url": msg.photo[-1].file_id}
    )
    await msg.answer(f"<code>{msg.photo[-1].file_id}</code>\nBu id orqali tovarni ochirib yuborishingiz mumkin")
    await msg.photo[-1].download(destination_dir=download_path)
    
    data = await state.get_data()
    product_name = data.get("product_name")
    product_size = data.get("product_size")
    product_count = data.get("product_count")
    product_price = data.get("product_price")
    product_url = data.get("product_url")
    await db.add_product(product_name, product_size, int(product_count), int(product_price), product_url)
    await msg.answer("Rahmat! Mahsulot bazaga saqlandi")
    await state.finish()


### delete PRODUCT Function
@dp.message_handler(Command("delete_product"), user_id=ADMINS)
async def delete_product(msg: types.Message):
    await msg.answer("mahsulot id sini tashlang")
    await Delete.product_id.set()

@dp.message_handler(state=Delete.product_id)
async def delete_product(msg: types.Message, state: FSMContext):
    await db.delete_product(msg.text)
    await msg.answer("Mahsulot ochib ketdi")
    await state.finish()