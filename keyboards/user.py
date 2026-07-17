from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():

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

    return keyboard
