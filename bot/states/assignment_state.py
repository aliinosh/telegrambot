from aiogram.fsm.state import StatesGroup, State


class AssignmentState(StatesGroup):

    topic = State()

    pages = State()
