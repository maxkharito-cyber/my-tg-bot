import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher

# Порт для Render
PORT = int(os.environ.get("PORT", 10000))

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    token = os.getenv("BOT_TOKEN")
    bot = Bot(token=token)
    dp = Dispatcher()

    # Запуск веб-сервера (чтобы Render не убивал бота)
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
