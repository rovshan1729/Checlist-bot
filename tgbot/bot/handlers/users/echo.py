import os

from aiogram import types

from tgbot.bot.utils import get_user
from tgbot.bot.loader import dp


@dp.message_handler(commands=["delolimpic"])
async def del_olimpic(message: types.Message):
    user = get_user(message.from_user.id)

    if user.is_olimpic:
        user.is_olimpic = False
        user.save(update_fields=["is_olimpic"])
        await message.answer("Olimpiada jarayonida o'chirildi!")
    else:
        await message.answer("Siz olimpiadani hali boshlamagansiz!")


@dp.message_handler(commands=["deluser"])
async def del_user(message: types.Message):
    user = get_user(message.chat.id)

    if user is not None and user.is_registered:
        user.is_registered = False
        user.save(update_fields=['is_registered'])
        await message.answer("You profile.is_registered = False")
    else:
        await message.answer("You are not registered")


@dp.message_handler(commands=["registered"])
async def reg_user(message: types.Message):
    chat_id = message.chat.id
    user = get_user(chat_id)
    print("works")
    if user is not None and not user.is_registered:
        user.is_registered = True
        user.save(update_fields=['is_registered'])
        await message.answer("You profile.is_registered = True")
    else:
        await message.answer("You are registered")
