from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states.presentation_state import PresentationState
from services.presentation_service import create_presentation

router = Router()


@router.message(lambda m: m.text == "📊 Presentation")
async def start_presentation(message: Message, state: FSMContext):

    await state.set_state(PresentationState.topic)

    await message.answer("Enter presentation topic")


@router.message(PresentationState.topic)
async def get_topic(message: Message, state: FSMContext):

    await state.update_data(topic=message.text)

    await state.set_state(PresentationState.slide_count)

    await message.answer("How many slides? (max 25)")


@router.message(PresentationState.slide_count)
async def get_slide_count(message: Message, state: FSMContext):

    count = int(message.text)

    await state.update_data(slides=count)

    await state.set_state(PresentationState.images)

    await message.answer("Add images? yes/no")


@router.message(PresentationState.images)
async def generate(message: Message, state: FSMContext):

    data = await state.get_data()

    topic = data["topic"]

    slides = data["slides"]

    with_images = message.text.lower() == "yes"

    await message.answer("Generating presentation...")

    path = create_presentation(topic, slides, with_images)

    await message.answer_document(
        document=open(path, "rb")
    )

    await state.clear()
