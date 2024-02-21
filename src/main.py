from config import TOKEN, ADMIN1, ADMIN2
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
import logging
import asyncio
from aiogram import F
from keyboards import main_kb

dp = Dispatcher()
bot = Bot(TOKEN)


@dp.message(CommandStart())
async def start_def(message: types.Message):
    await bot.send_message(text="Привет, пидор", chat_id=message.from_user.id, reply_markup=main_kb)

@dp.message(F.text == "Меню 🚀")
async def main_menu(message: types.Message):
    await bot.send_message(text="Приветствую в меню", chat_id=message.from_user.id)
    await start_def(message)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())