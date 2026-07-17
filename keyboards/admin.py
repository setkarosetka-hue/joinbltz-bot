from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def admin_menu():

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

    return keyboard
