from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from django.conf import settings
from tgbot.bot.loader import bot


def get_back_keyboard():
    back_button = InlineKeyboardButton(text="Назад", callback_data="back")
    return InlineKeyboardMarkup(row_width=1).add(back_button)
