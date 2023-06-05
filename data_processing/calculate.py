"""Модуль расчета количества билетов"""

import random
import time
from typing import Dict

from loguru import logger


class Calculate:
    """
    Клас для расчета количества номиналов для введенной сумы.
    Номиналы билетов выбираются из тех данных которые ввел пользователь.
    Выбор происходит рандомно.

    """

    choice_value = None
    input_data = None
    output_data = None

    @classmethod
    def _create_output_dict(cls, input_dict: Dict) -> None:
        cls.output_data = {
            key: {
                'count_tick': 0,
                'sum_count': 0,
                'end_num': 0,
                'tick_left': 0,
                'sum_left': 0,
            }
            for key in input_dict
        }
        cls.output_data['sum_money'] = 0

    @classmethod
    def calculate(cls, data: Dict[int, list[int, int]], money: int) -> Dict:
        cls._create_output_dict(data)

        cls.input_data = data
        cls.choice_value = [ticket for ticket, num in data.items() if num[1] > 0]

        start_work = time.time()
        while cls.output_data['sum_money'] != money and money > cls.output_data['sum_money']:

            if int(time.time() - start_work) >= 3:
                time_stop = int(time.time() - start_work)
                logger.error(f'Ошибка расчета, time - {time_stop} сек.')
                return cls.output_data

            try:
                chosen_ticket = random.choice(cls.choice_value)

            except IndexError as err:
                logger.error(err)
                return cls.output_data

            if not cls._check_number(chosen_ticket) or cls.output_data['sum_money'] + chosen_ticket > money:
                continue

            cls.output_data[chosen_ticket]['count_tick'] += 1
            cls.output_data[chosen_ticket]['sum_count'] += chosen_ticket
            cls.output_data['sum_money'] += chosen_ticket

            cls.input_data[chosen_ticket][0] += 1
            cls.input_data[chosen_ticket][1] -= 1

        for tick, val in cls.input_data.items():
            sum_left = val[1] * tick

            cls.output_data[tick]['end_num'] = val[0]
            cls.output_data[tick]['tick_left'] = val[1]
            cls.output_data[tick]['sum_left'] = sum_left

        return cls.output_data

    @classmethod
    def _check_number(cls, num: int) -> bool:

        if cls.input_data[num][1] != 0:
            return True

        cls.choice_value.remove(num)
        return False


if __name__ == '__main__':
    calcul = Calculate()
    summ = 1000
    data = {500: [5, 6], 400: [7, 8], 300: [6, 10]}
    res = calcul.calculate(data=data, money=summ)
    print(res)
