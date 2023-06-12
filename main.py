import sys

from aiogram import executor
from loguru import logger

from loader import dp, bot
from commands import calculate

logger.add(sink=sys.stdout, format="{time:/YYYY-MM-DD HH:mm:ss} {level} {message}")


async def on_start(_) -> None:
    """
    Функция, выводит в консоль сообщения, что бот работает.
    Запускает функции, для регистрации обработчиков команд ТГ-бота

    """

    try:
        logger.info('Bot start work')
        await calculate.Command.register_command(dp)

    except Exception as err:
        logger.exception(err)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
