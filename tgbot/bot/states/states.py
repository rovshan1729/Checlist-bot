from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from tgbot.bot.loader import dp
from tgbot.bot.keyboards.inline import get_back_keyboard


class Intro(StatesGroup):
    branch = State()
    name = State()
    confirm_reset = State()


class FirstSection(StatesGroup):
    s1q1 = State()
    s1q2 = State()
    s1q3 = State()
    s1q4 = State()
    s1q5 = State()
    s1q6 = State()
    s1q7 = State()
    s1q8 = State()
    s1q9 = State()
    s1q10 = State()
    s1q11 = State()
    s1q12 = State()
    s1q13 = State()
    s1q14 = State()
    final_s1 = State()

    
class SecondSection(StatesGroup):
    s2q1 = State()
    s2q2 = State()
    s2q3 = State()
    s2q4 = State()
    s2q5 = State()
    s2q6 = State()
    s2q7 = State()
    s2q8 = State()
    s2q9 = State()
    s2q10 = State()
    s2q11 = State()
    s2q12 = State()
    s2q13 = State()
    final_s2 = State()
    
class ThirdSection(StatesGroup):
    s3q1 = State()
    s3q2 = State()
    s3q3 = State()
    s3q4 = State()
    s3q5 = State()
    s3q6 = State()
    s3q7 = State()
    s3q8 = State()
    s3q9 = State()
    s3q10 = State()
    s3q11 = State()
    s3q12 = State()
    s3q13 = State()
    s3q14 = State()
    s3q15 = State()
    s3q16 = State()
    s3q17 = State()
    s3q18 = State()
    s3q19 = State()
    s3q20 = State()
    s3q21 = State()
    final_s3 = State()
    

class FourSection(StatesGroup):
    s4q1 = State()
    s4q2 = State()
    s4q3 = State()
    s4q4 = State()
    s4q5 = State()
    s4q6 = State()
    s4q7 = State()
    s4q8 = State()
    s4q9 = State()
    s4q10 = State()
    s4q11 = State()
    s4q12 = State()
    s4q13 = State()
    s4q14 = State()
    final_s4 = State()
    

class FifthSection(StatesGroup):
    s5q1 = State()
    s5q2 = State()
    s5q3 = State()
    s5q4 = State()
    s5q5 = State()
    s5q6 = State()
    s5q7 = State()
    s5q8 = State()
    s5q9 = State()
    s5q10 = State()
    s5q11 = State()
    s5q12 = State()
    s5q13 = State()
    s5q14 = State()
    s5q15 = State()
    s5q16 = State()
    s5q17 = State()
    s5q18 = State()
    s5q19 = State()
    s5q20 = State()
    final_s5 = State()
    

class SixSection(StatesGroup):
    s6q1 = State()
    s6q2 = State()
    s6q3 = State()
    s6q4 = State()
    s6q5 = State()
    s6q6 = State()
    s6q7 = State()
    s6q8 = State()
    s6q9 = State()
    final_s6 = State()
    

class SevenSection(StatesGroup):
    s7q1 = State()
    s7q2 = State()
    s7q3 = State()
    s7q4 = State()
    s7q5 = State()
    s7q6 = State()
    s7q7 = State()
    s7q8 = State()
    s7q9 = State()
    s7q10 = State()
    s7q11 = State()
    finale_s7 = State()
    

class TextQuestionSection(StatesGroup):
    t1q1 = State()
    t1q2 = State()
    t1q3 = State()
    t1q4 = State()
    
    
    


# @dp.message_handler(commands=['start'], state="*")
# async def start_handler_reset(message: types.Message, state: FSMContext):
#     await message.answer(
#         "<strong>Вы уверены, что хотите начать сначала и сбросить все данные?</strong>",
#         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
#             .add(types.KeyboardButton("Да"))
#             .add(types.KeyboardButton("Нет")),
#         parse_mode='HTML'
#     )
#     current_state = await state.get_state()
#     await state.update_data(previous_state=current_state)
#     await Intro.confirm_reset.set()

# @dp.message_handler(Text(equals="Да", ignore_case=True), state=Intro.confirm_reset)
# async def confirm_reset_handler(message: types.Message, state: FSMContext):
#     await state.finish()
#     await state.reset_data()
    
#     await message.answer(
#         "Начало с чистого листа.",
#         reply_markup=types.ReplyKeyboardRemove()
#     )

#     await message.answer(
#         "<strong>Здравствуйте! Какой филиал вы проверяете?</strong>",
#         reply_markup=(),
#         parse_mode='HTML'
#     )
#     await Intro.branch.set()
    


# @dp.message_handler(Text(equals="Нет", ignore_case=True), state=Intro.confirm_reset)
# async def cancel_reset_handler(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     previous_state = data.get('previous_state')
#     if previous_state:
#         await state.set_state(previous_state)

#     await message.answer(
#         "<strong>Продолжим с того места, где остановились.</strong>",
#         reply_markup=get_back_keyboard(),
#         parse_mode='HTML'
#     )
