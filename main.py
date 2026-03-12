from bot.handlers.start_handler import router as start_router
from bot.handlers.language_handler import router as language_router
from bot.handlers.presentation_handler import router as presentation_router
from bot.handlers.assignment_handler import router as assignment_router
from bot.handlers.settings_handler import router as settings_router
from bot.handlers.webapp_handler import router as webapp_router


dp.include_router(start_router)
dp.include_router(language_router)
dp.include_router(presentation_router)
dp.include_router(assignment_router)
dp.include_router(settings_router)
dp.include_router(webapp_router)
