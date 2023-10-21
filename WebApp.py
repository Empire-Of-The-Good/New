from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('API_BOT')
dp = Dispatcher(bot)
 
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб магазин', web_app=WebAppInfo(url='https://empire-of-the-good.github.io/WebSite/')))
    await message.answer("Вот держи:))",  reply_markup=markup)


executor.start_polling(dp)