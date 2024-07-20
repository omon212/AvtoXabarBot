from aiogram.dispatcher.filters.state import State, StatesGroup


class Xabar(StatesGroup):
    text = State()
    vaqt = State()

class Admin(StatesGroup):
    group_name = State()
    group_id = State()
    delete_id = State()
