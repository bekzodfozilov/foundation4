# from aiogram import Bot, Dispatcher, types, executor
# from markups import menu, products
#
# token = '7145822513:AAGEj31RHcqByL8F_SNwQ8sA-sGVI1_sBJU'
#
# bot = Bot(token=token, parse_mode='HTML')
#
# dp = Dispatcher(bot=bot)
#
#
# async def on_startup(_):
#     await bot.send_message(chat_id=1329197690,
#                            text='Bot ishga tushdi')
#     print('bot ishga tushdi')
#
#
# @dp.message_handler(commands=['start'])
# async def cm_start(message: types.Message):
#     await message.answer(
#         text="Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing\n\nShuningdek, aksiyalarni "
#              "ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin\n\n<a href='https://maxway.uz/uz'>menu</a>",
#         reply_markup=menu)
#
#
# @dp.message_handler(text='🛍 Buyurtma berish')
# async def product(message: types.Message):
#     await message.answer(text='Kategoriyani tanlang', reply_markup=products)
#
# if __name__ == '__main__':
#     executor.start_polling(dispatcher=dp, on_startup=on_startup, skip_updates=True)
