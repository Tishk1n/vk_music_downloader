from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = [
    [KeyboardButton(text='Меню 🚀')]
    ]
main_kb = ReplyKeyboardMarkup(keyboard=menu_button, resize_keyboard=True)