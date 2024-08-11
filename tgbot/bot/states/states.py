from aiogram.dispatcher.filters.state import State, StatesGroup

class Intro(StatesGroup):
    branch = State()
    name = State()

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