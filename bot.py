import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN

from database.sqlite import create_db

from handlers.start import router as start_router
from handlers.application import router as application_router
from handlers.admin import router as admin_router
from handlers.settings import router as settings_router


async def main():

    # Создание базы данных
    await create_db()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    # Подключение всех разделов
    dp.include_router(start_router)
    dp.include_router(application_router)
    dp.include_router(admin_router)
    dp.include_router(settings_router)

    print("✅ BLTZ JOIN BOT запущен")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
