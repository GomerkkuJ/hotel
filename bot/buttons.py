from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопка для получения номера телефона
def get_phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    number = KeyboardButton('Поделиться контактом', request_contact=True)

    kb.add(number)

    return kb