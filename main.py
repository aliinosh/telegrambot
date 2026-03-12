import asyncio
from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from bot.handlers import handle_message

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

dp.message.register(handle_message)


async def main():

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
