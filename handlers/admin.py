from database.sqlite import set_setting

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

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
                    text="📝 Изменить приветствие",
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


@router.callback_query(F.data == "stats")
async def stats(callback: CallbackQuery):

    await callback.message.answer(
        "📊 Статистика BLTZ\n\n"
        "👥 Пользователи: скоро\n"
        "📋 Заявки: скоро"
    )

    await callback.answer()


@router.callback_query(F.data == "welcome_edit")
async def welcome_edit(callback: CallbackQuery):

    await callback.message.answer(
        "📝 Редактор приветствия\n\n"
        "Скоро здесь можно будет изменить текст приветствия."
    )

    await callback.answer()

@router.callback_query(F.data == "welcome_edit")
async def welcome_edit(callback: CallbackQuery):

    await callback.message.answer(
        "📝 Отправь новый текст приветствия:"
    )

    await callback.answer()
