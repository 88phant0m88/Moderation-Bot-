import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я работаю на Amvera Cloud! 🚀\nНапиши мне что-нибудь!")

# Команда /info
@dp.message_handler(commands=['info'])
async def send_info(message: types.Message):
    await message.reply("Я бот для модерации\nСоздан с помощью Amvera")

# Обработка всех сообщений
@dp.message_handler()
async def echo(message: types.Message):
    text = message.text.lower()
    
    if 'привет' in text or 'hello' in text:
        await message.answer("Привет! 👋 Как дела?")
    elif 'как дела' in text:
        await message.answer("У меня всё отлично! А у тебя? 😊")
    elif 'спасибо' in text:
        await message.answer("Пожалуйста! 🙌")
    else:
        await message.answer(f"Я получил твоё сообщение: {message.text}\nЯ работаю! ✅")

if __name__ == '__main__':
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)

