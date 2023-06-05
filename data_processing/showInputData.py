def show(data: dict[int, list[int, int]], summ) -> str:
    _text = f'Вы указали следующие данные:\n<b>Сумма</b> для расчета - {summ} ₽.\n'

    for key, val in data.items():
        _text += '\n<b>Номинал</b> №{num}:\n<b>Стартовый номер:</b> {count}\n<b>Кол-во:</b> {start}\n'.format(
            num=key, count=val[0], start=val[1]
        )
    return _text
