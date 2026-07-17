from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import ADMIN_ID


router = Router()


class Application(StatesGroup):
    username = State()
    age = State()
    about = State()


@router.callback_query(F.data == "apply")
async def apply_start(callback: CallbackQuery, state: FSMContext):

    await callback.message.answer(
        "🎮 Напиши свой Roblox Username:"
    )

    await state.set_state(Application.username)
    await callback.answer()


@router.message(Application.username)
async def username(message: Message, state: FSMContext):

    await state.update_data(
        username=message.text
    )

    await message.answer(
        "🎂 Сколько тебе лет?"
    )

    await state.set_state(Application.age)


@router.message(Application.age)
async def age(message: Message, state: FSMContext):

    await state.update_data(
        age=message.text
    )

    await message.answer(
        "📝 Расскажи о себе:"
    )

    await state.set_state(Application.about)


@router.message(Application.about)
async def about(message: Message, state: FSMContext):

    data = await state.get_data()

    text = (
        "📥 <b>Новая заявка BLTZ</b>\n\n"
        f"🎮 Roblox: {data['username']}\n"
        f"🎂 Возраст: {data['age']}\n"
        f"📝 О себе: {message.text}\n\n"
        f"👤 Telegram: @{message.from_user.username}"
    )


    await message.bot.send_message(
        ADMIN_ID,
        text
    )


    await message.answer(
        "✅ Заявка отправлена администрации BLTZ!"
    )

    await state.clear()

 
