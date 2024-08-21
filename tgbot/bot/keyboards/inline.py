from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from django.conf import settings
from tgbot.bot.loader import bot


def get_back_keyboard():
    back_button = InlineKeyboardButton(text="Назад", callback_data="back")
    return InlineKeyboardMarkup(row_width=1).add(back_button)


def get_restart_confirmation_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("ДА", callback_data="confirm_restart"))
    keyboard.add(InlineKeyboardButton("НЕТ", callback_data="cancel_restart"))
    return keyboard