import sys

from aiogram import executor
from loguru import logger

from loader import dp, bot
from commands import get_data

logger.add(sink=sys.stdout, format="{time:/YYYY-MM-DD HH:mm:ss} {level} {message}")


async def on_start(_) -> None:
    """ Функция, выводит в консоль сообщения, что бот работает.
        Запускает функции, для регистрации обработчиков команд ТГ-бота

    """

    try:
        logger.info('Bot start work')
        await get_data.Command.register_command(dp)

    except Exception as err:
        logger.exception(err)

    # await bot.set_webhook(URL_APP)


# async def on_shutdown(dp):
#     await bot.delete_webhook()
#
# executor.set_webhook(
#     dispatcher=dp,
#     webhook_path='',
#     on_startup=on_start,
#     on_shutdown=on_shutdown,
#     skip_updates=True,
#
# )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
