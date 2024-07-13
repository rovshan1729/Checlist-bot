import re
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.exceptions import MessageNotModified, MessageToDeleteNotFound
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from bot.models import TelegramProfile, University
from bot.choices import OrganizationChoice
from common.models import Region, District, School, Class
from tgbot.bot.keyboards.inline import languages_markup, get_check_button, stop_test
from tgbot.bot.keyboards.reply import (phone_keyboard, main_markup, get_regions_markup, get_districts_markup, registration, back, generate_list_markup, get_university_markup,
                                       get_schools_markup, generate_start_markup, classes, main_menu_markup)
from tgbot.bot.loader import dp, bot
from tgbot.bot.loader import gettext as _
from tgbot.bot.states.main import AdmissionState
from tgbot.bot.utils import get_user, get_lang
from utils.subscription import get_result

from olimpic.models import UserQuestion


async def do_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")
    if not lang:
        user = get_user(message.from_user.id)
        if user:
            lang = user.language
    check_subs_message_id = data.get("check_subs_message_id")
    if check_subs_message_id:
        try:
            await bot.delete_message(message.from_user.id, check_subs_message_id)
        except MessageToDeleteNotFound:
            print("Delete is not working correctly!")
    user = TelegramProfile.objects.filter(telegram_id=message.from_user.id).first()
    if not user:
        TelegramProfile.objects.create(telegram_id=user.id, first_name=user.first_name, last_name=user.last_name,
                                       username=user.username, language=user.language_code,
                                       full_name=user.full_name)
    if not user.is_registered:
        photo="https://www.dropbox.com/scl/fi/c3ql5ucg986wyynwmmygb/Python.png?rlkey=p2b3pbgjeco26ofplxiyo12uo&st=xcwqllt4&dl=0"
        await message.answer_photo(
            photo=photo,
            caption='🏆 Boshqarma boshlig\'ining "Kelajak yoshlari" deb nomlangan <b>python</b> bo\'yicha onlayn Olimpiadasiga Xush kelibsiz!\n\n',
            reply_markup=registration(),
            parse_mode='HTML')
        await AdmissionState.organization_state.set()
    else:
        await message.answer(_("Bosh menyu"), reply_markup=main_markup(lang))


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    user = get_user(message.from_user.id)
    data = await state.get_data()
    if user.is_olimpic:
        await message.answer(f"Siz hozirda test jarayonidasiz!\nIltimos, testni tugating.\n\n"
                             f"Agar testan chiqish xolasengiz pasti tugmani bosing.\n"
                             f"<b>Testan chiqsangiz 0 ball olasiz!</b>",
                             reply_markup=stop_test(),
                             parse_mode='HTML')
        await AdmissionState.test_stop_check.set()

    else:
        await state.finish()

        final_status, chat_ids = await get_result(user_id=message.from_user.id)

        reply_markup = await get_check_button(chat_ids)

        if not final_status:
            if reply_markup:
                check_subs_message = await message.answer(
                    _(f"Quyidagi kanallarga obuna bo'lishingiz kerak, pastdagi tugmalar ustiga bosing ⬇️"),
                    reply_markup=reply_markup,
                    disable_web_page_preview=True)
                await state.update_data({"check_subs_message_id": check_subs_message.message_id})
            else:
                await do_start(message, state)
        else:
            await do_start(message, state)


@dp.callback_query_handler(lambda call: call.data == "stop_test", state=AdmissionState.test_stop_check)
async def get_stop_test(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")
    if not lang:
        user = get_user(call.from_user.id)
        if user:
            lang = user.language

    user = get_user(call.from_user.id)
    user.is_olimpic = False
    user.save(
        update_fields=["is_olimpic"]
    )
    last_question = UserQuestion.objects.filter(user=user).last()
    if last_question:
        try:
            user_id = last_question.user.telegram_id
            if last_question.message_id:
                await bot.delete_message(user_id, last_question.message_id)
        except Exception as e:
            print(e)
    await call.message.answer(f"Test toxtatildi\n"
                              f"Bosh menyu",
                              reply_markup=main_markup(lang))
    await call.message.delete()



@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")
    if not lang:
        user = get_user(call.message.from_user.id)
        if user:
            lang = user.language

    final_status, chat_ids = await get_result(user_id=call.from_user.id)
    if final_status:
        data = await state.get_data()
        check_subs_message_id = data.get("check_subs_message_id")
        if check_subs_message_id:
            try:
                await bot.delete_message(call.from_user.id, check_subs_message_id)
            except MessageToDeleteNotFound:
                await call.message.delete()
        user = TelegramProfile.objects.filter(telegram_id=call.from_user.id).first()
        if not user:
            TelegramProfile.objects.create(telegram_id=user.id, first_name=user.first_name, last_name=user.last_name,
                                           username=user.username, language=user.language_code,
                                           full_name=user.full_name)
        if not user.is_registered:
            photo="https://www.dropbox.com/scl/fi/c3ql5ucg986wyynwmmygb/Python.png?rlkey=p2b3pbgjeco26ofplxiyo12uo&st=xcwqllt4&dl=0"
            await call.message.answer_photo(
                photo=photo,
                caption='🏆 Boshqarma boshlig\'ining "Kelajak yoshlari" deb nomlangan ingliz tili bo\'yicha onlayn Olimpiadasiga Xush kelibsiz!\n\n',
                reply_markup=registration(),
                parse_mode='HTML')
            await AdmissionState.organization_state.set()
        else:
            await call.message.answer(_("Bosh menyu"), reply_markup=main_markup(lang))
    else:
        reply_markup = await get_check_button(chat_ids)
        if not reply_markup:
            await call.message.delete()
            await call.answer(_("Barcha kanallarga obuna bo'ldingiz!"))
        else:
            try:
                await call.message.edit_reply_markup(reply_markup=reply_markup)
            except MessageNotModified:
                await call.answer(_("Siz obuna bo'lmagan kanallar mavjud!"), show_alert=True)


@dp.callback_query_handler(state=AdmissionState.organization_state)
async def get_user_organization(call: types.CallbackQuery, state: FSMContext):
    user = get_user(call.from_user.id)
    choices = OrganizationChoice.labels
    if not user.is_registered:
        await call.message.answer("Qayerda o'qisiz?",
                                reply_markup=await generate_start_markup(choices))
        await call.message.delete()
        await AdmissionState.full_name.set()
    
    else:
        await call.message.answer(_("Siz qilgan o'zgarishlar saqlandi, iltimos botni /start bosib qayta ishga tushiring"),
                             reply_markup=types.ReplyKeyboardRemove())
        await state.finish()


@dp.message_handler(state=AdmissionState.full_name)
async def get_user_fullname(message: types.Message, state: FSMContext):
    choices = OrganizationChoice.labels
    user = get_user(message.from_user.id)
    if not user.is_registered:

        if message.text == 'Maktab':
            await state.update_data({"organization": message.text})
            await message.answer("Iltimos, familiyangizni, ismingizni va otangizning ismini kiriting ⬇️",
                                    reply_markup=back())
            await AdmissionState.self_introduction.set()

        elif message.text == "O\'quv markaz":
            await state.update_data({"organization": message.text})
            await message.answer("Iltimos, familiyangizni, ismingizni va otangizning ismini kiriting ⬇️",
                                 reply_markup=back())
            await AdmissionState.self_introduction.set()

        elif message.text == "Xususiy universitet":
            await state.update_data({"organization": message.text})
            await message.answer("Iltimos, familiyangizni, ismingizni va otangizning ismini kiriting ⬇️",
                                 reply_markup=back())
            await AdmissionState.self_introduction.set()

        elif message.text == "Davlat universitet":
            await state.update_data({"organization": message.text})
            await message.answer("Iltimos, familiyangizni, ismingizni va otangizning ismini kiriting ⬇️",
                                 reply_markup=back())
            await AdmissionState.self_introduction.set()
        else:
            await message.answer(_("Maktab, O'quv markaz, Xususiy universitet, Davlat universitet nomlangan davlatlarni tanlang"),
                                 reply_markup=await generate_start_markup(choices))

    else:
        await message.answer(_("Siz qilgan o'zgarishlar saqlandi, iltimos botni /start bosib qayta ishga tushiring"),
                             reply_markup=types.ReplyKeyboardRemove())
        await state.finish()


@dp.message_handler(state=AdmissionState.self_introduction)
async def self_introduction(message: types.Message, state: FSMContext):
    choices = OrganizationChoice.labels
    is_correct = [word for word in message.text.split(' ') if word.isalpha() and len(word) <= 20]

    if message.text == "🔙 Orqaga":
        await message.answer("Qayerda o'qisiz?",
                             reply_markup=await generate_start_markup(choices))
        await AdmissionState.full_name.set()
        
    elif message.text and 2 <= len(is_correct) <= 3 :
        await state.update_data({"self_introduction": message.text})
        await message.answer(_('Telefon raqamingizni quyidagi tugmani bosgan holda yuboring.'),
                             reply_markup=phone_keyboard)
        await AdmissionState.phone.set()
    else:
        await message.answer(_("Faqat Text Formatda Kamida 2ta so'z bilan yozing"))


@dp.message_handler(state=AdmissionState.phone, content_types=types.ContentType.TEXT)
@dp.message_handler(state=AdmissionState.phone, content_types=types.ContentType.CONTACT)
async def contact(message: types.Message, state: FSMContext):
    if message.content_type in types.ContentType.TEXT:
        await message.answer(_("Pastdagi tugma orqali raqamingizni yuboring"))
    elif message.content_type in types.ContentType.CONTACT and message.contact.phone_number and message.from_user.id == message.contact.user_id:
        await state.update_data({"phone": message.contact.phone_number})
        await message.answer(_("Tug'ilgan kuningizni kiriting.\n"
                               "Format 01.01.2000"), reply_markup=back())
        await AdmissionState.birth_date.set()
    else:
        await message.answer(_('📲 Iltimos Raqamni Yuborish Tugmasini Bosing'))


@dp.message_handler(state=AdmissionState.birth_date)
async def user_birth_date(message: types.Message, state: FSMContext):
    if message.text == "🔙 Orqaga":
        await message.answer("Telefon raqamingizni quyidagi tugmani bosgan holda yuboring.", 
                             reply_markup=phone_keyboard)
        await AdmissionState.self_introduction.set()
        
    pattern = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19[0-9]{2}|200[0-9]|201[0-9]|2020)$'    
    if re.match(pattern, message.text):
        regions = Region.objects.all()
        await state.update_data({"birth_date": message.text})
        data = await state.get_data()
        lang = data.get("language")
        if not lang:
            user = get_user(message.from_user.id)
            if user:
                lang = user.language
        await message.answer(_("Viloyatingizni tanlang"), reply_markup=await get_regions_markup(regions, lang))
        await AdmissionState.region.set()

    else:
        await message.answer(_("Tug'ilgan sanangizni to'g'ri formatda kiriting.\n\nMasalan: 01.01.2000 (tug'ilgan yilingiz 2000-yildan katta bo'lishi shart)"))


@dp.message_handler(state=AdmissionState.region)
async def user_region(message: types.Message, state: FSMContext):
    if message.text:
        data = await state.get_data()
        lang = data.get("language")
        if not lang:
            user = get_user(message.from_user.id)
            if user:
                lang = user.language

        region = Region.objects.filter(
            Q(title=message.text) | Q(title_uz=message.text) | Q(title_ru=message.text) | Q(title_en=message.text)
        ).first()
        if region is not None:
            districts = District.objects.filter(
                parent=region.id
            ).order_by('title')
            await state.update_data({"region_id": region.id})
            await message.answer(_("Tuman yoki shaharni tanlang"),
                                 reply_markup=await get_districts_markup(districts, lang))
            await AdmissionState.district.set()
        else:
            regions = Region.objects.all()
            await message.answer(_("Viloyatingizni tanlang"), reply_markup=await get_regions_markup(regions, lang))
    else:
        await message.answer(_("Iltimos To'g'ri Formatda Kiriting (16.07.2002)"))


@dp.message_handler(state=AdmissionState.district)
async def user_district(message: types.Message, state: FSMContext):
    
    if message.text:
        data = await state.get_data()
        lang = data.get("language")
        if not lang:
            user = get_user(message.from_user.id)
            if user:
                lang = user.language

        district = District.objects.filter(
            Q(title=message.text) | Q(title_uz=message.text) | Q(title_ru=message.text) | Q(title_en=message.text)
        ).first()
        
        organization = data.get("organization")
        if organization == OrganizationChoice.SCHOOL:
            if district is not None:
                schools = School.objects.filter(
                    district=district.id
                ).order_by('title')
                await state.update_data({"district_id": district.id})
                await message.answer(_("Maktabingizni tanlang"), reply_markup=await get_schools_markup(schools, lang))
                await AdmissionState.school.set()
            else:
                data = await state.get_data()
                districts = District.objects.filter(
                    parent=data.get("region_id")
                ).order_by('title')
                await message.answer(_("Tuman yoki shaharni tanlang"),
                                    reply_markup=await get_districts_markup(districts, lang))
        
        elif organization == OrganizationChoice.EDUCATION_CENTER:
            if district is not None:
                edu_centers = University.objects.filter(
                    district=district.id,
                    type=OrganizationChoice.EDUCATION_CENTER
                )
                await state.update_data({"district_id": district.id})
                await message.answer("Ta'lim markazi",
                        reply_markup=await get_university_markup(edu_centers, lang))
                await AdmissionState.education_center.set()
        
        elif organization == OrganizationChoice.STATE_UNIVERSITY:
            if district is not None:
                state_university = University.objects.filter(
                    district=district.id,
                    type=OrganizationChoice.STATE_UNIVERSITY    
                ).order_by('title')
                await state.update_data({"district_id": district.id})
                await message.answer("Davlat universitetini tanlang.",
                        reply_markup=await get_university_markup(state_university, lang))
                await AdmissionState.state_university.set()
                
        elif organization == OrganizationChoice.PRIVATE_UNIVERSITY:
            if district is not None:
                private_university = University.objects.filter(
                    district=district.id,
                    type=OrganizationChoice.PRIVATE_UNIVERSITY    
                ).order_by('title')
                await state.update_data({"district_id": district.id})
                await message.answer("Xususiy universitetini tanlang.",
                        reply_markup=await get_university_markup(private_university, lang))
                await AdmissionState.private_university.set() 

    else:
        await message.answer(_("Iltimos To'g'ri Formatda Kiriting (16.07.2002)"))


@dp.message_handler(state=AdmissionState.state_university)
async def user_state_university(message: types.Message, state: FSMContext):
    data = await state.get_data()
    state_university = University.objects.filter(
        title=message.text
    ).first()

    if state_university is not None:
        await state.update_data({"university_id": state_university.id, })

        await collect_user_data(message, state)

    else:

        lang = data.get("language")
        if not lang:
            user = get_user(message.from_user.id)
            if user:
                lang = user.language
        if message.text == _("🔙 Orqaga"):
            data = await state.get_data()

            districts = District.objects.filter(
                parent=data.get("region_id")
            ).order_by('title')
            await message.answer(_("Tuman yoki shaharni tanlang"),
                                 reply_markup=await get_districts_markup(districts, lang))
            await AdmissionState.district.set()

        else:
            state_university = University.objects.filter(
                district=data.get("district_id"),
                type=OrganizationChoice.STATE_UNIVERSITY
            ).order_by('title')
            await message.answer(_("Davlat universitetini tanlang."), reply_markup=await get_university_markup(state_university, lang))


@dp.message_handler(state=AdmissionState.private_university)
async def user_private_university(message: types.Message, state: FSMContext):
    data = await state.get_data()
    private_university = University.objects.filter(
        title=message.text
    ).first()

    if private_university is not None:
        await state.update_data({"university_id": private_university.id})
        await collect_user_data(message, state)

    else:
        lang = data.get("language")
        if not lang:
            user = get_user(message.from_user.id)
            if user:
                lang = user.language
        if message.text == _("🔙 Orqaga"):
            data = await state.get_data()
            districts = District.objects.filter(
                parent=data.get("region_id")
            ).order_by('title')
          

            await message.answer(_("Tuman yoki shaharni tanlang"),
                                 reply_markup=await get_districts_markup(districts, lang))
            await AdmissionState.district.set()
            
        else:
            private_university = University.objects.filter(
                district=data.get("district_id"),
                type=OrganizationChoice.PRIVATE_UNIVERSITY
            ).order_by('title')
            await message.answer(_("Maktabingizni tanlang"), reply_markup=await get_university_markup(private_university, lang))


@dp.message_handler(state=AdmissionState.education_center)
async def user_education_center(message: types.Message, state: FSMContext):
    data = await state.get_data()
    education_center = University.objects.filter(
        title=message.text
    ).first()

    if education_center is not None:
        await state.update_data({"director_organization": education_center.id, 'university_id': education_center})
        await collect_user_data(message, state)

    else:
        lang = data.get("language")
        if not lang:
            user = get_user(message.from_user.id)
            if user:
                lang = user.language
        if message.text == _("🔙 Orqaga"):
            data = await state.get_data()
            districts = District.objects.filter(
                parent=data.get("region_id")
            ).order_by('title')
          

            await message.answer(_("Tuman yoki shaharni tanlang"),
                                 reply_markup=await get_districts_markup(districts, lang))
            await AdmissionState.district.set()
            
        else:
            education_center = University.objects.filter(
                district=data.get("district_id"),
                type=OrganizationChoice.EDUCATION_CENTER
            ).order_by('title')
            await message.answer(_("Maktabingizni tanlang"), reply_markup=await get_university_markup(education_center, lang))


@dp.message_handler(state=AdmissionState.school)
async def user_school(message: types.Message, state: FSMContext):
    if message.text:
        school = School.objects.filter(
            Q(title=message.text) | Q(title_uz=message.text) | Q(title_ru=message.text) | Q(title_en=message.text)
        ).first()
        if school is not None:
            await state.update_data({"school_id": school.id})
            await message.answer(_("Sinfingizni Tanlang"),
                                 reply_markup=classes)
            await AdmissionState.collect_data.set()
        else:
            data = await state.get_data()
            lang = data.get("language")
            if not lang:
                user = get_user(message.from_user.id)
                if user:
                    lang = user.language

            data = await state.get_data()
            schools = School.objects.filter(
                district=data.get("district_id")
            ).order_by('title')
            await message.answer(_("Maktabingizni tanlang"), reply_markup=await get_schools_markup(schools,lang))
    else:
        await message.answer(_("Iltimos Tugmalardan Birini Tanlang"))


@dp.message_handler(state=AdmissionState.collect_data)
async def collect_user_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("language")
    if not lang:
        user = get_user(message.from_user.id)
        if user:
            lang = user.language
    # is_in_class = any(message.text == class_tuple[0] for class_tuple in Class)

    # if is_in_class:
    #     user = TelegramProfile.objects.filter(
    #         telegram_id=message.from_user.id
    #     ).first()
    if user:
        user.full_name = data.get("self_introduction")
        user.phone_number = data.get("phone")
        user.birth_day = datetime.strptime(data.get("birth_date"), "%d.%m.%Y").date()
        user.region_id = data.get("region_id")
        user.district_id = data.get("district_id")
        user.school_id = data.get("school_id")
        user.organization = data.get("organization")
        user.university_id = data.get("university_id")
        user.class_room = message.text
        user.is_registered = True
        user.save(
            update_fields=["full_name", "phone_number", "birth_day", "region", "district", "school", "class_room", "organization", "university_id",
                            "is_registered"])
    else:
        TelegramProfile.objects.create(
            telegram_id=message.from_user.id,
            full_name=data.get("self_introduction"),
            phone_number=data.get("phone"),
            birth_day=datetime.strptime(data.get("birth_date"), "%d.%m.%Y").date(),
            region_id=data.get("region_id"),
            district_id=data.get("district_id"),
            school_id=data.get("school_id"),
            organization=data.get("organization"),
            university=data.get("university_id"),
            class_room=message.text,
            is_registered=True,
        )
    await message.answer(text=_("Ma'lumotlaringiz qabul qilindi"), reply_markup=main_markup(lang))
    await state.reset_data()
    await state.finish()
