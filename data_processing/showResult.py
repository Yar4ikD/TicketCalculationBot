import datetime
from docxtpl import DocxTemplate

from template.templatePath import baseFilePath, returnFilePath


def result_formation(data: dict):
    text = f"Сума расчета {data['sum_money']}₽\n\n<b>Билеты:</b>\n"
    for key in data:

        if isinstance(key, str):
            continue
        text += "\n<b>Номинал:</b> {num}\n<b>Взято кол-во</b>: {count}" \
                "\n<b>На сумму:</b> {sum_c}" \
                "\n<b>Осталось кол:</b> {left}" \
                "\n<b>На сумму:</b> {sum_l}" \
                "\n<b>Конечный номер:</b> {end_n}\n".format(num=key,
                                                            count=data[key]['count_tick'],
                                                            sum_c=data[key]['sum_count'],
                                                            left=data[key].get('tick_left', 0),
                                                            sum_l=data[key].get('sum_left', 0),
                                                            end_n=data[key].get('end_num', 0)
                                                            )

    return text


def create_template(data: dict):
    date = datetime.datetime.now()

    context = {
        'tickets': [
            {'denomination': key,
             'count': data[key]['count_tick'],
             'sum_count': data[key]['sum_count'],
             'left': data[key]['tick_left'],
             'sum_left': data[key]['sum_left'],
             'end_number': data[key]['end_num'],
             }
            for key in data if isinstance(key, int)
        ],

        'sum_money': str(data['sum_money']),
        'date': f'{date.day}/{date.month}/{date.year}год.'
    }

    with open(baseFilePath, 'rb') as file:
        doc = DocxTemplate(file)
        doc.render(context=context)

        doc.save(returnFilePath)
        file.close()

    return returnFilePath
