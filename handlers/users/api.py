from loader import dp, db, bot
from aiogram import types
import requests

@dp.message_handler(text="Dogs")
async def bot_start(message: types.Message):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    dog_img = response.json().get("message")
    dog_capt = response.json().get("status")
    await message.answer_photo(photo=dog_img, caption=dog_capt)