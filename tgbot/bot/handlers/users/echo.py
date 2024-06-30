from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.bot.utils import get_user
from tgbot.bot.loader import dp
from bot.models import TelegramProfile


@dp.message_handler(commands=["deluser"])
async def del_user(message: types.Message):
    chat_id = message.chat.id
    user = get_user(chat_id)

    if user is not None and user.is_registered:
        user.is_registered = False
        user.save(update_fields=['is_registered'])
        await message.answer("You profile.is_registered = False")
    else:
        await message.answer("You are not registered")


