from loader import dp
from aiogram import types


@dp.message_handler(text="To'lov qilish")
async def paid_func(msg: types.Message):
    await msg.answer("To'lov qilish")