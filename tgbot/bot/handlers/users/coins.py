from aiogram import types
from aiogram.types import InputFile
from tgbot.bot.utils import get_user
from aiogram.dispatcher import FSMContext
from tgbot.bot.loader import dp, bot
from bot.models import Product, UserProduct
from tgbot.bot.states.main import MainState, MarketState
from tgbot.bot.keyboards.reply import main_markup, get_coins_kb, back
from bot.models import TelegramProfile


@dp.message_handler(text="💸My Coins💰", state="*")
async def get_coins_main_menu(message: types.Message):
    tg_user = get_user(message.from_user.id)
    try:
        await message.answer(f'Salom {tg_user.first_name}',
                             reply_markup=types.ReplyKeyboardRemove())
        await message.answer(f'Sizni telegram bot akauntizda {tg_user.coins} coinla bor.',
                             reply_markup=get_coins_kb())
        await MarketState.main.set()
    except TelegramProfile.DoesNotExist:
        await message.answer("Profiliz topilmadi.")


@dp.message_handler(text="🔙 Orqaga", state="*")
async def back_to_main(message: types.Message):
    await message.answer("Bosh menu", reply_markup=main_markup())
    await MainState.main.set()

message_ids = []

@dp.message_handler(text="Shop", state=MarketState.main)
async def get_shop(message: types.Message, state: FSMContext):
    tg_user = get_user(message.from_user.id)
    products = Product.objects.all()

    async with state.proxy() as data:
        data['quantities'] = {}

    for product in products:
        name = product.title
        price = product.price
        photo_path = product.photo.path
        photo = InputFile(photo_path)
        quantity = 1
        async with state.proxy() as data:
            data['quantities'][product.id] = quantity
        await message.answer("Barcha productla",
                             reply_markup=types.ReplyKeyboardRemove())
        msg = await message.answer_photo(caption=f"Nomi: {name}\nNarxi: {price} coins\nMiqdori: {quantity}",
                                         photo=photo,
                                         reply_markup=types.InlineKeyboardMarkup(
                                             inline_keyboard=[
                                                 [
                                                     types.InlineKeyboardButton(
                                                         text="-", callback_data=f"subtract_{product.id}"
                                                     ),
                                                     types.InlineKeyboardButton(
                                                         text="+", callback_data=f"add_{product.id}"
                                                     )
                                                 ],
                                                 [
                                                     types.InlineKeyboardButton(
                                                         text="Xarid qilish", callback_data=f"buy_{product.id}"
                                                     )
                                                 ]
                                             ]
                                         ))

        message_ids.append(msg.message_id)
    await message.answer("Birini tanglang",
                         reply_markup=back())
    await MarketState.buy_product.set()


@dp.callback_query_handler(lambda call: call.data.startswith("buy_"), state=MarketState.buy_product)
async def buy_product(call: types.CallbackQuery, state: FSMContext):
    try:
        product_id = int(call.data.split("_")[1])

        user = get_user(call.from_user.id)
        product = Product.objects.get(id=product_id)

        async with state.proxy() as data:
            quantity = data['quantities'].get(product_id, 1)

            total_price = product.price * quantity

            if user.coins < total_price:
                await call.message.answer(
                    "Sizda yetarli miqdorda coin yo'q. Coinlarni yig'ish uchun Python-simulyator test qiling.")
                return

            user.coins -= total_price
            user.save()

            user_product = UserProduct.objects.create(user=user, product_id=product_id, quantity=quantity)
            tg_user = user_product.user.username
            phone_number = user_product.user.phone_number
            product = user_product.product
            quantity = user_product.quantity
            print(f"Username: {tg_user}\n\n"
                    f"Product va narxi: {product}\n\n"
                    f"Soni: {quantity}\n\n"
                    f"Telefon raqami: {phone_number}")
            await bot.send_message(chat_id=2124744962, text=f"Username: {tg_user}\n\n"
                                                            f"Product va narxi: {product}\n\n"
                                                            f"Soni: {quantity}\n\n"
                                                            f"Telefon raqami: {phone_number}")

            for message_id in message_ids:
                try:
                    await bot.delete_message(chat_id=call.message.chat.id, message_id=message_id)
                except Exception as delete_error:
                    print(f"Failed to delete message {message_id}: {delete_error}")

        await call.message.answer(
            "Xarid uchun raxmat\nSizning buyurtmangiz qabul qilindi. Administratorlar siz bilan tez orada bog'lanishadi.",
            reply_markup=main_markup())
        await MainState.main.set()

    except Exception as e:
        await call.message.answer(f"Xatolik yuz berdi: {e}")


@dp.callback_query_handler(lambda call: call.data.startswith("add_") or call.data.startswith("subtract_"),
                           state=MarketState.buy_product)
async def modify_quantity(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        product_id = int(call.data.split("_")[1])
        quantities = data['quantities']

        if call.data.startswith("add_"):
            quantities[product_id] += 1
        elif call.data.startswith("subtract_") and quantities[product_id] > 1:
            quantities[product_id] -= 1

        quantity = quantities[product_id]

        product = Product.objects.get(id=product_id)
        price = product.price

        original_caption = call.message.caption.split('\n')
        name = original_caption[0]
        total = price * quantity
        updated_caption = f"{name}\nNarxi: {total} coins\nMiqdori: {quantity}"

        await call.message.edit_caption(
            caption=updated_caption,
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(
                            text="-", callback_data=f"subtract_{product_id}"
                        ),
                        types.InlineKeyboardButton(
                            text="+", callback_data=f"add_{product_id}"
                        )
                    ],
                    [
                        types.InlineKeyboardButton(
                            text="Xarid qilish", callback_data=f"buy_{product_id}"
                        )
                    ]
                ]
            )
        )

    await call.answer()


