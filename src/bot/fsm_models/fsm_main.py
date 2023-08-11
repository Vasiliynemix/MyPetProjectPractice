from aiogram.fsm.state import StatesGroup, State


class FSMMainUser(StatesGroup):
    start = State()


class FSMMainAdmin(StatesGroup):
    start = State()
    add_admin = State()
