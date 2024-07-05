import os

from aiogram import types

from tgbot.bot.utils import get_user
from tgbot.bot.loader import dp
from pytube import YouTube


@dp.message_handler(commands=["deluser"])
async def del_user(message: types.Message):
    chat_id = message.chat.id
    user = get_user(chat_id)

    if user is None and user.is_registered:
        user.is_registered = False
        user.save(update_fields=['is_registered'])
        await message.answer("You profile.is_registered = False")
    else:
        await message.answer("You are not registered")


@dp.message_handler(commands=["registered"])
async def reg_user(message: types.Message):
    chat_id = message.chat.id
    user = get_user(chat_id)
    print("works")
    if user is not None and not user.is_registered:
        user.is_registered = True
        user.save(update_fields=['is_registered'])
        await message.answer("You profile.is_registered = True")
    else:
        await message.answer("You are registered")


@dp.message_handler(commands=["send_video"])
async def send_video(message: types.Message):
    # Youtubni direct pasharasiga karab olas urlni
    youtube_url = "https://youtu.be/Jh4szJHwaog"
    video_path = download_youtube_video(youtube_url)

    if video_path:
        with open(video_path, 'rb') as video:
            await message.answer_video(video)
        # localga download qilib kegn udalit qivoradi send bo'lganidan kegn
        os.remove(video_path)


def download_youtube_video(url: str) -> str:
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4', res="1080").first()
        if not stream:
            stream = yt.streams.filter(file_extension='mp4').first()
        if stream:
            file_path = stream.download(output_path="/home/rovshan/Documents/video/")
            return file_path
        else:
            print("resolution tugirlash kere")
            return None
    except Exception as e:
        print(f"xato qilding brat: {e}")
        return None