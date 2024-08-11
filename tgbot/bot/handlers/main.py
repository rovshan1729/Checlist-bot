from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext

from tgbot.bot.states.states import Intro, FirstSection, SecondSection
from tgbot.bot.loader import dp
from tgbot.models import Section, SectionNumberChoices 
from tgbot.bot.keyboards.inline import get_back_keyboard


dp.middleware.setup(LoggingMiddleware())


@dp.callback_query_handler(lambda c: c.data == 'back', state='*')
async def process_back_button(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    
    current_state = await state.get_state()
    data = await state.get_data()
    total_ball = data.get('total_ball', 0)
    questions = data.get('questions', [])

    if current_state == FirstSection.s1q2.state:
        previous_state = FirstSection.s1q1
        total_ball -= int(data.get('s1q1', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[0].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q3.state:
        previous_state = FirstSection.s1q2
        total_ball -= int(data.get('s1q2', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[1].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q4.state:
        previous_state = FirstSection.s1q3
        total_ball -= int(data.get('s1q3', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[2].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q5.state:
        previous_state = FirstSection.s1q4
        total_ball -= int(data.get('s1q4', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[3].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q6.state:
        previous_state = FirstSection.s1q5
        total_ball -= int(data.get('s1q5', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[4].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q7.state:
        previous_state = FirstSection.s1q6
        total_ball -= int(data.get('s1q6', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[5].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q8.state:
        previous_state = FirstSection.s1q7
        total_ball -= int(data.get('s1q7', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[6].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q9.state:
        previous_state = FirstSection.s1q8
        total_ball -= int(data.get('s1q8', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[7].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q10.state:
        previous_state = FirstSection.s1q9
        total_ball -= int(data.get('s1q9', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[8].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q11.state:
        previous_state = FirstSection.s1q10
        total_ball -= int(data.get('s1q10', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[9].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q12.state:
        previous_state = FirstSection.s1q11
        total_ball -= int(data.get('s1q11', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[10].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q13.state:
        previous_state = FirstSection.s1q12
        total_ball -= int(data.get('s1q12', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[11].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == FirstSection.s1q14.state:
        previous_state = FirstSection.s1q13
        total_ball -= int(data.get('s1q13', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[12].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
        
        """
            Next section 
        """
    elif current_state == SecondSection.s2q1.state:
        previous_state = FirstSection.s1q14
        # need to fix it 
        total_ball -= int(data.get('s1q14', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[13].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q2.state:
        previous_state = SecondSection.s2q1
        total_ball -= int(data.get('s2q1', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[0].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q3.state:
        previous_state = SecondSection.s2q2
        total_ball -= int(data.get('s2q2', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[1].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q4.state:
        previous_state = SecondSection.s2q3
        total_ball -= int(data.get('s2q3', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[2].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q5.state:
        previous_state = SecondSection.s2q4
        total_ball -= int(data.get('s2q4', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[3].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q6.state:
        previous_state = SecondSection.s2q5
        total_ball -= int(data.get('s2q5', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[4].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q7.state:
        previous_state = SecondSection.s2q6
        total_ball -= int(data.get('s2q6', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[5].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q8.state:
        previous_state = SecondSection.s2q7
        total_ball -= int(data.get('s2q7', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[6].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q9.state:
        previous_state = SecondSection.s2q8
        total_ball -= int(data.get('s2q8', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[7].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q10.state:
        previous_state = SecondSection.s2q9
        total_ball -= int(data.get('s2q9', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[8].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q11.state:
        previous_state = SecondSection.s2q10
        total_ball -= int(data.get('s2q10', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[9].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q12.state:
        previous_state = SecondSection.s2q11
        total_ball -= int(data.get('s2q11', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[10].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    elif current_state == SecondSection.s2q13.state:
        previous_state = SecondSection.s2q12
        total_ball -= int(data.get('s2q12', 0))
        text = f'<strong>{questions[0].section.title}</strong>\n\n{questions[11].title}\n\nОцените, пожалуйста, от 0 до 100 баллов.'
    else:
        await callback_query.message.answer("Вы вернулись в главное меню.\nНажмите /start")
        await state.finish()
        return

    if callback_query.message.text != text or callback_query.message.reply_markup != get_back_keyboard():
        await callback_query.message.edit_text(text, reply_markup=get_back_keyboard(),
                                               parse_mode='HTML')

    await state.update_data(total_ball=total_ball)
    await previous_state.set()


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("<strong>Здравствуйте! Какой филиал вы проверяете?</strong>",
                         reply_markup=get_back_keyboard(),
                         parse_mode='HTML')
    await Intro.branch.set()


@dp.message_handler(state=Intro.branch)
async def branch_handler(message: types.Message, state: FSMContext):
    await state.update_data(branch=message.text)
    await message.answer("<strong>Введите полное имя проверяющего.</strong>",
                        reply_markup=get_back_keyboard(),
                        parse_mode='HTML')
    await Intro.name.set()


@dp.message_handler(state=Intro.name)
async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    sections = Section.objects.filter(type=SectionNumberChoices.FIRST).first()
    questions = list(sections.section_questions.order_by('order'))
    await state.update_data(questions=questions)
    
    await message.answer(f'<strong>{sections.title}</strong>\n\n{questions[0].title}\n\n'
                         f'Оцените, пожалуйста, от 0 до 100 баллов.',
                          reply_markup=get_back_keyboard(),
                          parse_mode='HTML')
    await FirstSection.s1q1.set()
    
    
@dp.message_handler(state=FirstSection.s1q1)
async def s1q1_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q1=int(message.text))
            total_ball = int(message.text)
            await state.update_data(total_ball=total_ball)
            data = await state.get_data()
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[1].title}\n\n'
                                 f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                  reply_markup=get_back_keyboard(),
                                  parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=FirstSection.s1q2)
async def s1q2_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q2=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[2].title}\n\n'
                                 f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                  reply_markup=get_back_keyboard(),
                                  parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=FirstSection.s1q3)
async def s1q3_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q3=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[3].title}\n\n'
                                 f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                  reply_markup=get_back_keyboard(),
                                  parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=FirstSection.s1q4)
async def s1q4_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q4=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[4].title}\n\n'
                                 f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                  reply_markup=get_back_keyboard(),
                                  parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")


@dp.message_handler(state=FirstSection.s1q5)
async def s1q5_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q5=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[5].title}\n\n'
                                 f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                  reply_markup=get_back_keyboard(),
                                  parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")


@dp.message_handler(state=FirstSection.s1q6)
async def s1q6_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q6=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[6].title}\n\n'
                                 f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
     
        
@dp.message_handler(state=FirstSection.s1q7)
async def s1q7_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q7=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[7].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        

@dp.message_handler(state=FirstSection.s1q8)
async def s1q8_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q8=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[8].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        

@dp.message_handler(state=FirstSection.s1q9)
async def s1q9_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q9=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[9].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        

@dp.message_handler(state=FirstSection.s1q10)
async def s1q10_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q10=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[10].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        

@dp.message_handler(state=FirstSection.s1q11)
async def s1q11_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q11=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[11].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=FirstSection.s1q12)
async def s1q12_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q12=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[12].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
    
@dp.message_handler(state=FirstSection.s1q13)
async def s1q13_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q13=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', []) 
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[13].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            await FirstSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=FirstSection.s1q14)
async def s1q14_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s1q14=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            
            section = Section.objects.filter(type=SectionNumberChoices.FIRST).first()
            total_questions = section.total_questions
            
            first_section_result = (total_ball // total_questions) * 0.2
            await state.update_data(first_section_result=first_section_result)
            total_ball = 0
            await state.update_data(total_ball=total_ball)
            
            section = Section.objects.filter(type=SectionNumberChoices.SECOND).first()
            questions = list(section.section_questions.order_by('order'))
            await state.update_data(questions=questions)
            
            await message.answer(f'<strong>Вы перешли на другую секцию</strong>')
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[0].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
        
            await SecondSection.s2q1.set()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")


@dp.message_handler(state=SecondSection.s2q1)
async def s2q1_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q1=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[1].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q2)
async def s2q2_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q2=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[2].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q3)
async def s2q3_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q3=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[3].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q4)
async def s2q4_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q4=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[4].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q5)
async def s2q5_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q5=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[5].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q6)
async def s2q6_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q6=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[6].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q7)
async def s2q7_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q7=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[7].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")


@dp.message_handler(state=SecondSection.s2q8)
async def s2q8_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q8=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[8].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q9)
async def s2q9_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q5=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[9].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q10)
async def s2q10_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q10=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[10].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q11)
async def s2q11_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q11=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[11].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q12)
async def s2q12_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q12=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            questions = data.get('questions', [])
            
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[12].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")
        
        
@dp.message_handler(state=SecondSection.s2q13)
async def s2q13_handler(message: types.Message, state: FSMContext):
    try:
        if 0 <= int(message.text) <= 100:
            await state.update_data(s2q13=int(message.text))
            data = await state.get_data()
            total_ball = data.get('total_ball')
            total_ball += int(message.text)
            await state.update_data(total_ball=total_ball)
            
            section = Section.objects.filter(type=SectionNumberChoices.SECOND).first()
            total_questions = section.total_questions
            
            second_section_result = (total_ball // total_questions) * 0.2
            await state.update_data(second_section_result=second_section_result)
            total_ball = 0
            await state.update_data(total_ball=total_ball)
            
            section = Section.objects.filter(type=SectionNumberChoices.THIRD).first()
            questions = list(section.section_questions.order_by('order'))
            await state.update_data(questions=questions)
            
            await message.answer(f'<strong>Вы перешли на другую секцию</strong>')
            await message.answer(f'<strong>{questions[0].section.title}</strong>\n\n{questions[0].title}\n\n'
                                f'Оцените, пожалуйста, от 0 до 100 баллов.',
                                reply_markup=get_back_keyboard(),
                                parse_mode='HTML')
            
            await SecondSection.next()
        else:
            await message.answer("Ошибка! Баллы должны быть между 0 и 100.")
    except ValueError:
        await message.answer("Ошибка! Пожалуйста, введите число.")