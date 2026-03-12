import asyncio

from bot.bot import bot, dp

from bot.handlers.start_handler import router as start_router
from bot.handlers.language_handler import router as language_router
from bot.handlers.presentation_handler import router as presentation_router
from bot.handlers.assignment_handler import router as assignment_router
from bot.handlers.settings_handler import router as settings_router
from bot.handlers.webapp_handler import router as webapp_router

from storage.storage_manager import init_storage


async def main():

    # storage papkalarini yaratish
    init_storage()

    # routerlarni ulash
    dp.include_router(start_router)
    dp.include_router(language_router)
    dp.include_router(presentation_router)
    dp.include_router(assignment_router)
    dp.include_router(settings_router)
    dp.include_router(webapp_router)

    # botni ishga tushirish
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
