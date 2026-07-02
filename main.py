import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Порт для Render
PORT = int(os.environ.get("PORT", 10000))

async def handle(request):
    return web.Response(text="Бот работает!")

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Ошибка: Токен не найден!")
        return

    bot = Bot(token=token)
    dp = Dispatcher()

    # --- ЭТОТ БЛОК ОТВЕЧАЕТ ЗА КОМАНДЫ ---
    @dp.message(Command("start"))
    async def cmd_start(message: Message):
        await message.answer("Привет! Я ваш бот, и я работаю! 🎉")

    @dp.message()
    async def echo_handler(message: Message):
        await message.answer(f"Вы прислали мне: {message.text}")
    # ------------------------------------

    # Запуск веб-сервера (чтобы Render не убивал бота)
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
