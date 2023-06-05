from aiogram import types
from aiogram.dispatcher import FSMContext
from loguru import logger

from text.commandsText import after_out


async def stop_working(callback: types.Message, state: FSMContext) -> None:
    """
    Функция-обработчик, останавливает FSM состояния команд ТГ-бота.
    Выходит из команды(FSM состояния) и сообщает пользователю об удачному выходе из раздела.

    Args:
        callback: Передает объект - входящий запрос обратного вызова с кнопки
        state: Передает экземпляр класса State, FSM состояния бота.

    Returns: None

    """
    now_state = await state.get_state()
    logger.info(f"{now_state}")
    if now_state is None:
        return

    await state.finish()
    await callback.answer(text=after_out)
