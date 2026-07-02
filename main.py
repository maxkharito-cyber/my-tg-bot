import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher

PORT = int(os.environ.get("PORT", 10000))

async def handle(request):
    return web.Response(text="Бот работает!")

async def start_web_server():
    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    print(f"Веб-сервер запущен на порту {PORT}")

async def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("Ошибка: Токен не найден!")
        return
    
    bot = Bot(token=token)
    dp = Dispatcher()
    
    await start_web_server()
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
