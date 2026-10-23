import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8307089020:AAHpFr3ly_fUj_wcK3vS7edpMbm5eu5rSRs"

dp = Dispatcher()

@dp.message(Command("start))
async def cmd_start(message: types.Message):
await message.answer("Привет! Хочешь дружить со мною?")

async def main():
 await dp.star_polling(bot)
if __name__ == "__main__"
asyncio.run(main())
