from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📋 Подать заявку",
                    callback_data="apply"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📜 Правила BLTZ",
                    callback_data="rules"
                )
            ]
        ]
    )

    await message.answer(
        "⚡ <b>Добро пожаловать в BLTZ!</b>\n\n"
        "🛡️ Здесь ты можешь подать заявку на вступление в клан.\n\n"
        "Нажми кнопку ниже, чтобы начать.",
        reply_markup=keyboard
    )
