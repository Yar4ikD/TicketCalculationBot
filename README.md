<p>
</p>
  
<div id="header" align="center">
  <img src="https://media.giphy.com/media/cJFQJzZxFMhONxDTnt/giphy.gif" width="100"/>
</div>

<h1 align="center">TelegramBotCalculate</h1>  
<h3 align="center">The main language of the bot is Russian.</h3>  

<div align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" title="Python" alt="Python"/>&nbsp;
  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram"/>&nbsp;
  <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" title="Git" alt="Git"/>&nbsp;
  <img src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green" title="PyCharm" alt="PyCharm"/>&nbsp;
  <img src="https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white" title="Debian" alt="Debian"/>&nbsp;
</div>

The Telegram bot is written in Python using the Aiogram library. 
The main command of the bot is the calculation of the sum from the terms specified by the user. 
The amount is the amount of money. The terms are the denominations of the tickets. 
The user specifies the initial number of the ticket and the number of tickets of a certain denomination. 
Denominations (terms) that can be selected by the user: 

- 500, 400, 300, 250, 200, 150, 100, 50. 
- 
The calculation of the sum is implemented using the algorithm - Breadth-first search, BFS (Breadth-first search)

## Beginning of work
### Basic steps to get the bot running:
1. Get the bot's **\<token\>**
2. Install dependencies from the [requirements. txt](python_basic_diploma/requirements.txt)
```
venv\Scripts\activate.bat - Windows;
source venv/bin/activate - Linux и MacOS.
```
```
pip install -r requirements.txt
```
3. Create **.env** file in the root of the project and add:   
```
TOKEN=
YANDEX_API_KEY=
```

## Bot project structure
- main.py (The file that contains the bot object)
- loader.py (Bot initialization)
- config.py (File with settings)
- requirements.txt (Libraries)
- commands/ (Package - processing user commands)
- template/ (Package - templates)
- view/ (Package - presenting the result to the user)
- ticket/ (Package - storage class, ticket information processing)
- keyboard/ (Package - keyboard and buttons)
- utils/ (Package - utilities for processing information received from the user)
- text/ (Package - info lines)

## Bot commands

### Team - Start
Launching the bot and the command to calculate the amount.
- [/start, start]()


#### Modules responsible for the work of the command:

```
commands/
    calculation.py
```

```python
async def start(cls, message: types.Message, state: FSMContext) -> None:
```

### Command - Shut down
Stops the bot.

[//]: # (<img src="images/command-help.jpg" width="500">)

#### Modules responsible for the work of the command:

```
commands/
    base.py
```

```python
async def stop_working(callback: types.Message, state: FSMContext) -> None:
```






