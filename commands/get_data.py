import os

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from loguru import logger

from commands.base import stop_working
from data_processing.calculate import Calculate
from data_processing.checking import DataCheck
from data_processing.showInputData import show
from data_processing.showResult import result_formation, create_template
from keyboard.input_data import Buttons
from text.commandsText import (information_start,
                               choose_ticket,
                               left_data_entry,
                               get_ticket_error,
                               enter_start_number,
                               err_st_num_or_amount,
                               changed_section
                               )


class Command(StatesGroup):
    """
        Подкласс наследует от базового класса StatesGroup.
        В классе прописана работа команды ТГ-бота: .
        Приватные атрибуты класса это FSM состояние ТГ-бота.
    """
    _money = State()
    _get_ticket = State()
    _start_number = State()
    _amount = State()
    _result = State()

    tickets = {'500₽': 500, '400₽': 400, '300₽': 300, '250₽': 250, '200₽': 200, '150₽': 150, '100₽': 100, '50₽': 50}
    current_value = None
    input_data = dict()
    money = 0

    @classmethod
    async def start(cls, message: types.Message, state: FSMContext) -> None:
        """
        Метод класса запускает процесс работы команды ТГ-бота: Расчет количество взятых билетов для введенной суммы.
        Запускает машинное состояние бота - FSM _money.
        Выводит пользователю информацию о дальнейшем взаимодействии, пользователя с командой ТГ-бота.

        Args:
            message: Передает объект - входящий запрос обратного вызова с кнопки
            state: Передает класс FSM состояния бота.

        Returns: None

        """
        logger.info(f'User id: {message.from_user.id}')
        await cls._money.set()  # запускаем FSM состояния бота
        await message.answer(text=information_start)

    @classmethod
    async def sum_money(cls, message: types.Message, state: FSMContext) -> None:
        """
        Обработчик события - получение суммы денег, для которой будет производиться расчет.

        Args:
            message: Сообщение от пользователя
            state: Машинное состояние ТГ-бота.

        Returns: None

        """

        if message.text == Buttons.skip_but.text and cls.money:
            await cls._get_ticket.set()
            await message.answer(text=choose_ticket, reply_markup=Buttons.ticket_numbers())

        else:
            try:
                cls.money = int(message.text)

                assert cls.money > 999, 'Сума меньше 1000'
                assert cls.money % 2 == 0, 'Сума не кратна 2'
                assert cls.money % 10 == 0, 'Число не заканчивается на 0'

                await cls._get_ticket.set()
                await message.answer(text=choose_ticket, reply_markup=Buttons.ticket_numbers())

            except (ValueError, AssertionError) as err:
                logger.debug(f'Указанные данные не корректны -> {err}')

                await message.reply(text='Jib,rf')

    @classmethod
    async def ticket_value(cls, message: types.Message, state: FSMContext) -> None:
        """
        Обработчик события - получения номинала билета.

        Args:
            message: Сообщение от пользователя
            state: Машинное состояние ТГ-бота.

        Returns: None

        """

        if message.text == Buttons.complete_input_but.text:
            await cls._result.set()
            await message.answer(text=left_data_entry, reply_markup=Buttons.view_calculate())

        else:
            try:
                cls.current_value = cls.tickets[message.text]

                await cls._start_number.set()
                await message.answer(text=enter_start_number, reply_markup=ReplyKeyboardRemove())

            except KeyError:
                logger.debug(f'Пользователь не нажал на список, ввел данные -> {message.text}')
                await message.reply(text=get_ticket_error)

    @classmethod
    async def start_number(cls, message: types.Message, state: FSMContext) -> None:
        """
        Обработчик события - получения начального номера билета.

        Args:
            message: Сообщение от пользователя
            state: Машинное состояние ТГ-бота.

        Returns: None

        """

        try:
            cls.input_data[cls.current_value] = [abs(int(message.text))]

            await cls._amount.set()
            await message.answer('Принято!\nКакое кол-во билета?.')

        except ValueError:
            logger.error(f'Ошибка ввода начального номера > {message.text}')
            await message.reply(text=err_st_num_or_amount)

    @classmethod
    async def amount(cls, message: types.Message, state: FSMContext) -> None:
        """
        Обработчик события - получения кол-ва билета определенного номинала.

        Args:
            message: Сообщение от пользователя
            state: Машинное состояние ТГ-бота.

        Returns: None

        """

        try:
            cls.input_data[cls.current_value].append(abs(int(message.text)))
            await cls._get_ticket.set()
            await message.answer(text='Принято!\nПродолжаем.', reply_markup=Buttons.ticket_numbers())

        except ValueError:
            logger.error(f'Ошибка ввода количества билетов -> {message.text}')
            await message.reply(text=err_st_num_or_amount)

    @classmethod
    async def display_result(cls, message: types.Message, state: FSMContext):

        if message.text == Buttons.view_data_but.text:  # выводим данные которые ввел пользователь
            msg = show(cls.input_data, cls.money)
            await message.answer(text=msg, reply_markup=Buttons.calculate())

        elif message.text == Buttons.return_input_data.text:  # возвращаем пользователя в блок ввода суммы денег
            await cls._money.set()
            await message.answer(text=changed_section, reply_markup=Buttons.skip())

        elif message.text == Buttons.calculate_but.text:  # запускаем расчет и выводи результат
            if DataCheck.money_and_tickets(input_data=cls.input_data, money=cls.money):  # если сумма билетов >= денег
                result = Calculate.calculate(data=cls.input_data, money=cls.money)
                file_path = create_template(data=result)

                msg = result_formation(data=result)
                await message.answer(text=msg, reply_markup=Buttons.return_input_or_out())

                try:
                    file = open(file_path, 'rb')

                except FileNotFoundError as err:
                    logger.exception(err)
                    await message.answer('Ошибка отправки файла! Обратитесь к администратору.')
                else:
                    await message.answer_document(file)

                # finally:
                #     file.close()

            else:
                logger.debug('Сумма билетов, меньшая суммы денег')
                await message.answer(
                    text='Сумма билетов, <b>меньшая</b> суммы денег.',
                    reply_markup=Buttons.return_input_or_out()
                )

        else:
            await message.reply('Я не понимаю что мне делать.')

    @classmethod
    async def register_command(cls, dp: Dispatcher) -> None:
        """
        Метод класса регистрирует обработчики сообщений, декораторы.
        Args:
            dp: Передает класс Dispatcher.

        Returns: None

        """
        dp.register_message_handler(cls.start, Text(equals=['start', 'старт', '/start'], ignore_case=True), state=None)
        dp.register_message_handler(stop_working, Text(Buttons.but_out.text), state='*')
        dp.register_message_handler(callback=cls.sum_money, state=cls._money)

        dp.register_message_handler(callback=cls.ticket_value, state=cls._get_ticket)
        dp.register_message_handler(callback=cls.start_number, state=cls._start_number)
        dp.register_message_handler(callback=cls.amount, state=cls._amount)

        dp.register_message_handler(callback=cls.display_result, state=cls._result)
