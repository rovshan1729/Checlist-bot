from django.conf import settings
from tgbot.models import TelegramProfile as User

def get_user(telegram_id):
    user = User.objects.filter(telegram_id=telegram_id).first()
    return user
