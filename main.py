from aiogram import executor

from loader import dp, bot
from commands import calculation
from loggerSetup.loggers import root


async def on_start(_) -> None:
    """
    Функция, выводит в консоль сообщения, что бот работает.
    Запускает функции, для регистрации обработчиков команд ТГ-бота

    """

    try:
        root.info("Bot start work")
        await calculation.Command.register_command(dp)

    except Exception as err:
        root.exception(err)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
