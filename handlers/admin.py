from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID

router = Router()


@router.message(Command("panel"))
async def panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📋 Заявки",
                    callback_data="applications"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢 Рассылка",
                    callback_data="broadcast"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📝 Редактор приветствия",
                    callback_data="welcome_edit"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📊 Статистика",
                    callback_data="stats"
                )
            ]
        ]
    )

    await message.answer(
        "👑 <b>Админ-панель BLTZ</b>",
        reply_markup=keyboard
    )
