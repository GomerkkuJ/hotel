from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):
    get_name_state = State()
    get_number_state = State()
    get_email_state = State()


class Booking(StatesGroup):
    get_country_state = State()
    get_city_state = State()
    get_state_state = State()
    get_hotel_state = State()


