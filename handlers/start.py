from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from keyboards.user import main_menu

router = Router()


@router.message(Command("start"))
async def start(message: Message):

    photo = FSInputFile(
        "images/bltz_logo.png"
    )

    await message.answer_photo(
        photo=photo,
        caption=
        "⚡ <b>Добро пожаловать в BLTZ!</b>\n\n"
        "🛡️ Бот для вступления в наш проект.\n\n"
        "Нажми кнопку ниже, чтобы подать заявку.",
        reply_markup=main_menu()
    )
