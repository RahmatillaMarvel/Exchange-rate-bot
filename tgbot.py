import logging
from aiogram import Bot, Dispatcher, executor, types
from ExchangeRate import CurrencyData

API_TOKEN = 'BOT_TOKEN'

USD = "USD"
RUB = "RUB"
UZS = "UZS"
som = "so'm"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu aleykum. Bizning valyuta hisoblagich botimizga xush kelibsiz! \n Dollar qiymatini ko'rish uchun /usd buyrug'idan foydalaning \n Rubl qiymatini ko'rish uchun /rub buyrug'idan foydalaning \n\n Hisoblashda $, rubl yoki so'm so'zlaridan foydalaning")
@dp.message_handler(commands=['usd'])
async def send_welcome(message: types.Message):
    await message.reply(f"1$ - {CurrencyData(USD, UZS)} so'm")
@dp.message_handler(commands=['rub'])
async def send_welcome(message: types.Message):
    await message.reply(f"1 rubl - {CurrencyData(RUB, UZS)} so'm")

@dp.message_handler()
async def currencyCalculate(message: types.Message):
    if "$" in message.text:      
        await message.answer(f"{int(message.text.replace('$', '').replace(' ', ''))*CurrencyData(USD, UZS)} so'm")
    elif "rubl" in message.text:
        await message.answer(f"{round(int(message.text.replace('rubl', '').replace(' ', ''))*CurrencyData(RUB, UZS), 2)} so'm")
    elif "som" or "so'm" in message.text:
        await message.answer(f"{round(int(message.text.replace(som, '').replace('som', '').replace(' ', ''))/CurrencyData(USD, UZS), 2)} dollar")
        await message.answer(f"{round(int(message.text.replace(som, '').replace('som', '').replace(' ', ''))/CurrencyData(USD, UZS), 2)} dollar")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)