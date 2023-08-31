"""В этом модуле созданы базовые кнопки ТГ-бота."""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class UniversalButtons:
    """
    Базовый класс, в котором прописаны часто используемые кнопки ТГ-бота.
    """

    but_command_again = KeyboardButton(text="Запусти команду заново.")
    but_out = KeyboardButton(text="Завершить работу")

    @classmethod
    def out_or_return(cls) -> ReplyKeyboardMarkup:
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons.add(cls.but_out)

        return buttons
