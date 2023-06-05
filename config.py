import os
from dotenv import load_dotenv, find_dotenv

"""
Модуль содержит конфигурацию, токены, ключи  для запуска и работы ТГ-бота.

"""

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
URL_APP = os.getenv('URL_APP')
