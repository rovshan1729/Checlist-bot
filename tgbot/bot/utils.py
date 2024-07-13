from django.conf import settings
from bot.models import TelegramProfile as User
from olimpic.models import UserQuestion


def get_lang(language):
    lang_code = None
    languages = settings.LANGUAGES
    for lang in languages:
        if lang[1] == language:
            lang_code = lang[0]
    return lang_code


async def get_lang_code(state):
    data = await state.get_data()
    language = data.get("lang")
    return get_lang(language)


def get_user(telegram_id):
    user = User.objects.filter(telegram_id=telegram_id).first()
    return user


def reset_correct_answers(user):
    UserQuestion.objects.filter(user=user, is_correct=True).delete()
    