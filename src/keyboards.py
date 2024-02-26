from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_button = [
    [KeyboardButton(text='Меню 🚀')]
    ]
main_kb = ReplyKeyboardMarkup(keyboard=menu_button, resize_keyboard=True)

buttons_list = [
    [
    InlineKeyboardButton(text="Поиск плейлистов", callback_data="find_playlist")
    ],
    [
    InlineKeyboardButton(text="Настройки", callback_data="settings")
    ],
    [
    InlineKeyboardButton(text="Регистрация", callback_data="registration")
    ]
]
menu_kb = InlineKeyboardMarkup(inline_keyboard=buttons_list)
