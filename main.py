import os
from aiogram import Bot, Dispatcher, executor, types

# Токен из переменных окружения тест
API_TOKEN = os.getenv('BOT_TOKEN')

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот на Amvera Cloud! 🚀")

# Обработчик всех сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Вы написали: {message.text}")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)

####### будет вывод
