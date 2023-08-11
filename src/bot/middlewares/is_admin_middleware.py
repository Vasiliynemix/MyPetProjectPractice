from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from src.db.queries import user_queries


class IsAdmin(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        session_maker = data['session_maker']
        user = await user_queries.get_user_by_id(message=event, session_maker=session_maker)
        if user.is_admin:
            data['is_admin'] = True
            return await handler(event, data)
        else:
            await event.answer('У вас нет прав пользоваться данной функцией, извините')
            return False

