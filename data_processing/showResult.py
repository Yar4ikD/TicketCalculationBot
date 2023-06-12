import datetime
from typing import Union, Dict

from docxtpl import DocxTemplate

from data_processing.node import Node
from template.templatePath import baseFilePath, returnFilePath


def standard_format(data: Dict[Union[int, str], Union[Node, str, int]]) -> str:
    """
    Функция создает, заполняет данными и возвращает строку.
    Срока возвращается пользователю, в которой записанный результат работы команды (calculate) ТГ-бота.

    Args:
        data: Словарь из данными о билетах и расчетной суммы.

    Returns: text

    """

    text = f"Сума расчета {data['sum_money']}₽\n\n<b>Билеты:</b>\n"
    for key in data:

        if isinstance(key, str):
            continue
        text += "\n<b>Номинал:</b> {num}\n<b>Взято кол-во</b>: {taken}" \
                "\n<b>На сумму:</b> {sum_t}" \
                "\n<b>Осталось кол:</b> {left}" \
                "\n<b>На сумму:</b> {sum_l}" \
                "\n<b>Конечный номер:</b> {end_n}\n".format(num=key,
                                                            taken=data[key].taken_tickets,
                                                            sum_t=data[key].taken_sum,
                                                            left=data[key].left,
                                                            sum_l=data[key].left_sum,
                                                            end_n=data[key].end_number
                                                            )

    return text


def file_format(data: Dict[Union[int, str], Union[Node, str, int]]) -> str:
    date = datetime.datetime.now().strftime('%d-%m-%Y')

    context = {
        'tickets': [
            {'denomination': key,
             'count': data[key].taken_tickets,
             'sum_count': data[key].taken_sum,
             'left': data[key].left,
             'sum_left': data[key].left_sum,
             'end_number': data[key].end_number,
             }
            for key in data if isinstance(key, int)
        ],

        'sum_money': str(data['sum_money']),
        'date': date,
        'error': data.get('error', '')
    }

    with open(baseFilePath, 'rb') as file:
        doc = DocxTemplate(file)
        doc.render(context=context)

        doc.save(returnFilePath)
        file.close()

    return returnFilePath
