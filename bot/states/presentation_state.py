from aiogram.fsm.state import StatesGroup
from aiogram.fsm.state import State


class PresentationState(StatesGroup):

    topic = State()

    slide_count = State()

    images = State()
