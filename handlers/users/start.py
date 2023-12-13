from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.registrState import Registr
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.default.menu_btn import menu_choice_btn

@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    
    # with open(f"inbazar_data/files/check.txt", 'w+') as file:
    #     file.write('fskl;gjwhp')
        
    #     await bot.send_document(chat_id=message.from_user.id, document=file)
    
    await message.answer(f"Salom, {message.from_user.full_name}!")

    user_id = message.from_user.id
    is_user_member = await db.select_user(telegram_id=int(user_id))

    if is_user_member==None:
        await message.answer("To'liq ism familya kiriting")
        await Registr.full_name.set()
    else:
        await message.answer(f"☺ Botimizga xush kelibsiz", reply_markup=menu_choice_btn)
    
@dp.message_handler(state=Registr.full_name)   
async def get_full_name(msg: types.Message, state: FSMContext):
    await state.update_data(
        {f"full_name": msg.text}
    )
    await msg.answer("Telefon raqamingizni kiriting")
    await Registr.phone_number.set()

@dp.message_handler(state=Registr.phone_number)
async def get_phone_number(msg: types.Message, state: FSMContext):
    await state.update_data(
        {"phone_number": msg.text}
    )
    
    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    
    await state.finish()
    await db.add_user(msg.from_user.id, full_name, phone_number, msg.from_user.username)
    await msg.answer("Raxmat! Ro'yhatdan o'tdingiz.", reply_markup=menu_choice_btn)