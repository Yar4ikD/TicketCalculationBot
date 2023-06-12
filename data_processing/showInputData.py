from typing import Dict

from data_processing.node import Node


def show(data: Dict[int, Node], summ: int) -> str:
    _text = f'Вы указали следующие данные:\n<b>Сумма</b> для расчета - {summ} ₽.\n'

    for key, node in data.items():
        _text += '\n<b>Номинал</b> №{num}:\n<b>Стартовый номер:</b> {count}\n<b>Кол-во:</b> {start}\n'.format(
            num=key, count=node.count, start=node.start_number
        )
    return _text
