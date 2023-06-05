from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboard.base import UniversalButtons


class Buttons(UniversalButtons):
    """
        Класс наследует от базового класса UniversalButtons.
        Методы класса отвечают за создание кнопок и клавиатуры ТГ-Бота.
    """

    choose_tickets = ['500₽', '400₽', '300₽', '250₽', '200₽', '150₽', '100₽', '50₽']
    tickets_but = [KeyboardButton(text=text) for text in choose_tickets]

    view_data_but = KeyboardButton(text='Показать введенные данные')
    skip_but = KeyboardButton(text='Пропустить.')
    calculate_but = KeyboardButton(text='Рассчитать')
    complete_input_but = KeyboardButton(text='Завершить ввод данных')
    return_input_data = KeyboardButton('Ввести еще данные')

    @classmethod
    def ticket_numbers(cls) -> ReplyKeyboardMarkup:
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons.add(*cls.tickets_but)
        buttons.add(cls.complete_input_but)

        return buttons

    @classmethod
    def view_calculate(cls) -> ReplyKeyboardMarkup:
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons.add(cls.view_data_but)
        buttons.add(cls.calculate_but)

        return buttons

    @classmethod
    def skip(cls) -> ReplyKeyboardMarkup:
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons.add(cls.skip_but)

        return buttons

    @classmethod
    def calculate(cls) -> ReplyKeyboardMarkup:
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons.add(cls.calculate_but)
        buttons.add(cls.return_input_data)

        return buttons

    @classmethod
    def return_input_or_out(cls) -> ReplyKeyboardMarkup:
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        buttons.add(cls.view_data_but)
        buttons.add(cls.return_input_data)
        buttons.add(cls.but_out)

        return buttons
