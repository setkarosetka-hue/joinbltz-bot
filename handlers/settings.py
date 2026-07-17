from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data == "rules")
async def rules(callback: CallbackQuery):

    await callback.message.answer(
        "📜 <b>Правила BLTZ</b>\n\n"
        "1. Уважать участников.\n"
        "2. Не использовать читы.\n"
        "3. Соблюдать правила клана."
    )

    await callback.answer()
