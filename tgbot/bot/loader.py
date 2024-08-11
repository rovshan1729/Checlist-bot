from src.settings import API_TOKEN, REDIS_HOST, REDIS_PORT, REDIS_DB
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.conf import settings
from .middlewares.localization import Localization

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2(
#     host=REDIS_HOST,
#     port=REDIS_PORT,
#     db=REDIS_DB,
# )
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


