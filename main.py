import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_TOKEN = "8875658721:AAHX4Rs4UQApvMtygYMVzl-4Cct34CYQy4c"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ твой первый бот на Python.")

@dp.message()
async def echo_handler(message: types.Message):
    if message.text:
        await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())