import requests
from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

import states
from states import *
import buttons
import database

bot = Bot('')
dp = Dispatcher(bot, storage=MemoryStorage())

main_url = 'http://127.0.0.1:5000'

@dp.message_handler(state=states.Registration.get_name_state)
async def get_user_name(message, state=states.Registration.get_name_state):
    user_id = message.from_user.id

    username = message.text

    await state.update_data(name=username)

    await message.answer('Отправьте номер телефона', reply_markup=buttons.get_phone_number_kb())

    await states.Registration.get_number_state.set()



@dp.message_handler(state=states.Registration.get_number_state, content_types=['contact'])
async def get_user_number(message, state=states.Registration.get_number_state):
    user_id = message.from_user.id

    user_contact = message.contact.phone_number


    user_data = await state.get_data()
    user_name = user_data.get('name')

    # Отправляем post запрос на регистрацию в наш quiz_api и получаем уникальный айди для пользователя
    register_url = main_url + f'/register/{user_name}/{user_contact}'
    response = requests.post(register_url)

    # Получаем ответ в виде json
    data = response.json()  # -> {'status': 1, 'user_id': some integer}

    # регистрируем на локальную базу уже нашего бота
    database.register_user_db(user_tg_id=user_id, user_quiz_id=data.get('user_id'))

    # Отправляем ответ
    await message.answer(f'Вы успешно зарегистрированы\nВаш идентификатор: {data.get("user_id")}',
                         reply_markup=buttons.main_menu_kb())

    # Завершаем процесс регистрации
    await state.finish()
