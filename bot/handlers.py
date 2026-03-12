from aiogram.types import Message
from ai.content_generator import generate_slides
from presentation.slide_parser import parse_slides
from presentation.ppt_generator import create_presentation


async def handle_message(message: Message):

    topic = message.text

    await message.answer("AI taqdimot yaratmoqda...")

    text = generate_slides(topic)

    slides = parse_slides(text)

    file = create_presentation(slides)

    await message.answer_document(open(file, "rb"))
