from aiogram import types
from aiogram.dispatcher import FSMContext
from tgbot.bot.handlers.main import start_handler
from tgbot.bot.loader import dp
from tgbot.bot.keyboards.inline import get_restart_confirmation_keyboard

@dp.message_handler(commands=['restart'], state="*")
async def restart_command_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await start_handler(message)
    
    #1.4000000000000001%