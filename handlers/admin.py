from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID


router = Router()


@router.message(Command("panel"))
async def admin_panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        return


    await message.answer(
        "👑 <b>Админ-панель BLTZ</b>\n\n"
        "📋 Заявки\n"
        "📢 Рассылка\n"
        "⚙️ Настройки\n"
        "📊 Статистика"
    )
