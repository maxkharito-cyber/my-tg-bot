import os
import asyncio
from aiogram import Bot, Dispatcher

# Получаем токен из переменных окружения Render
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    if not BOT_TOKEN:
        print("Ошибка: Токен не найден! Проверьте настройки в Render.")
        return
    
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
