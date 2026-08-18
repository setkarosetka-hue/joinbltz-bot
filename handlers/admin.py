from database.sqlite import set_setting

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import ADMIN_ID

router = Router()


class WelcomeEdit(StatesGroup):
    text = State()


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
                    text="⚙️ Редактор приветствия",
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


@router.callback_query(F.data == "applications")
async def applications(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Доступ запрещен", show_alert=True)
        return

    await callback.message.answer(
        "📋 <b>Заявки BLTZ</b>\n\n"
        "Скоро здесь можно будет просмотреть и обработать заявки."
    )

    await callback.answer()


@router.callback_query(F.data == "stats")
async def stats(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Доступ запрещен", show_alert=True)
        return

    await callback.message.answer(
        "📊 <b>Статистика BLTZ</b>\n\n"
        "👥 Пользователи: скоро\n"
        "📋 Заявки: скоро"
    )

    await callback.answer()


@router.callback_query(F.data == "broadcast")
async def broadcast(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Доступ запрещен", show_alert=True)
        return

    await callback.message.answer(
        "📢 <b>Рассылка</b>\n\n"
        "Скоро здесь можно будет отправить рассылку пользователям."
    )

    await callback.answer()


@router.callback_query(F.data == "welcome_edit")
async def welcome_button(callback: CallbackQuery, state: FSMContext):

    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Доступ запрещен", show_alert=True)
        return

    await callback.message.answer(
        "📝 Отправь новый текст приветствия BLTZ:"
    )

    await state.set_state(WelcomeEdit.text)

    await callback.answer()


@router.message(WelcomeEdit.text)
async def save_welcome(message: Message, state: FSMContext):

    if message.from_user.id != ADMIN_ID:
        return

    await set_setting(
        "welcome",
        message.text
    )

    await message.answer(
        "✅ Приветствие BLTZ изменено!"
    )

    await state.clear()
