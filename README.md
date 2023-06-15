<p>
</p>
  
<div id="header" align="center">
  <img src="https://media.giphy.com/media/cJFQJzZxFMhONxDTnt/giphy.gif" width="100"/>
</div>

<h1 align="center">TelegramBotCalculate</h1>  

<div align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" title="Python" alt="Python"/>&nbsp;
  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/>&nbsp;
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" title="Git" alt="Git"/>&nbsp;
  <img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green" title="PyCharm" alt="PyCharm"/>&nbsp;
  <img src="https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white" title="Debian" alt="Debian"/>&nbsp;
</div>

Телеграм бот написан на Python, с использованием библиотеки Aiogram.  
Основная команда бота это - расчет суммы из слагаемых, указанных пользователем. Сумма - это количество денег.  
Слагаемые - это номиналы билетов. 
Пользователь указывает начальный номер билета и кол-во билетов определенного номинала.  
Номиналы(слагаемы) которые могут быть выбраны пользователем:

- 500, 400, 300, 250, 200, 150, 100, 50. 

Расчет суммы реализован с помощью алгоритма - Поиск в ширину, BFS(Breadth-first search)

## Начало работы
### Основные шаги для запуска работы бота:
1. Получить **\<token\>** бота  
2. Установить зависимости с файла [requirements. txt](python_basic_diploma/requirements.txt)
```
venv\Scripts\activate.bat - для Windows;
source venv/bin/activate - для Linux и MacOS.
```
```
pip install -r requirements.txt
```
3. В корне проекта создать файл **.env** и добавить:
```
TOKEN=
YANDEX_API_KEY=
```

## Структура проекта бота 
- main.py (Файл, который содержит объект бота)
- loader.py (Инициализация бота)
- config.py (Файл с настройками)
- requirements.txt (Библиотеки)
- commands/ (Пакет - обработка команд пользователя)
- template/ (Пакет - шаблоны)
- view/ (Пакет - представление результата пользователю)
- ticket/ (Пакет - класс хранение, обработка информации о билетах)
- keyboard/ (Пакет - клавиатура и кнопки)
- utils/ (Пакет - утилиты обработки полученной информации от пользователя)
- text/ (Пакет - информационные строки)

## Команды бота

### Команда - Старт
Запуск бота и команду расчета суммы.
- [/start, start, старт]()


#### Модули отвечающие за работу команды:

```
commands/
    calculation.py
```

```python
async def start(cls, message: types.Message, state: FSMContext) -> None:
```

### Команда - Завершить работу
Останавливает работу бота.

[//]: # (<img src="images/command-help.jpg" width="500">)

#### Модули отвечающие за работу команды:

```
commands/
    base.py
```

```python
async def stop_working(callback: types.Message, state: FSMContext) -> None:
```






