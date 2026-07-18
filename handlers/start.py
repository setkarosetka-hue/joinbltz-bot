from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.user import main_menu
from database.sqlite import get_setting


router = Router()


@router.message(Command("start"))
async def start(message: Message):

    # Получаем приветствие из базы
    welcome = await get_setting("welcome")

    if not welcome:
        welcome = (
            "⚡ <b>Добро пожаловать в BLTZ!</b>\n\n"
            "🛡️ Бот для вступления в наш клан.\n\n"
            "Нажми кнопку ниже, чтобы подать заявку."
        )


    await message.answer(
        text=welcome,
        reply_markup=main_menu()
    )
