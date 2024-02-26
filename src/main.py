from config import TOKEN, ADMIN
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import logging
import asyncio
from aiogram import F, Router
from keyboards import main_kb, menu_kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

dp = Dispatcher()
bot = Bot(TOKEN)

router = Router()

class Registration(StatesGroup):
    name = State()
    age = State()
    number = State()


@dp.message(CommandStart())
async def start_def(message: types.Message):
    await bot.send_message(text="Привет, пидор", chat_id=message.from_user.id, reply_markup=main_kb)

@dp.message(F.text == "Меню 🚀")
async def main_menu(message: types.Message):
    await bot.send_message(text="Приветствую в меню", chat_id=message.from_user.id, reply_markup=menu_kb)

@dp.callback_query(F.data == "registration")
async def start_registration(call: CallbackQuery, state: FSMContext):
    await state.set_state(Registration.name)
    await call.message.answer("Введите Ваше имя.")

@dp.message(Registration.name)
async def fsm_age(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите Ваш возраст")
    await state.set_state(Registration.age)

@dp.message(Registration.age)
async def fsm_number(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите Ваш номер телефона.")
    await state.set_state(Registration.number)

@dp.message(Registration.number)
async def fsm_end(message: types.Message, state:FSMContext):
    await state.update_data(number=message.text)
    await message.answer("Спасибо за регистрацию! Загрузка ваших данных.")
    data = await state.get_data()
    await message.answer(f"Ваше имя: {data['name']}\nВаш возраст {data['age']}\nВаш номер телефона: {data['number']}")
    print(f"Ваше имя: {data['name']}\nВаш возраст {data['age']}\nВаш номер телефона: {data['number']}")
    await state.clear()

@dp.callback_query(F.data == "admin-panel")
async def admin_panel(call: CallbackQuery):
    if call.from_user.id == ADMIN:
        await call.message.answer("Ты админ")
    else:
        await call.message.answer("Ты не админ")


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())