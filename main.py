import os
from aiogram import Bot, Dispatcher, executor, types

# Получаем токен
API_TOKEN = os.getenv('BOT_TOKEN')

# ПРОВЕРКА: Если токена нет, выводим ошибку в логи
if not API_TOKEN:
    print("❌ ОШИБКА: Переменная BOT_TOKEN не найдена!")
    print("Проверьте настройки проекта в Amvera -> Переменные")
    # Принудительно останавливаем бота, чтобы не висел
    exit(1) 
else:
    print("✅ Токен найден, запускаем бота...")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я работаю! 🚀")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Получил: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

