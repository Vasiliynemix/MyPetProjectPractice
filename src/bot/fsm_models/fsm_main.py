from aiogram.fsm.state import StatesGroup, State


class FSMMainUser(StatesGroup):
    start = State()


class FSMMainAdmin(StatesGroup):
    start = State()
    list_categories = State()
    add_admin = State()
