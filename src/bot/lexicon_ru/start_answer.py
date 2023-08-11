from aiogram.types import Message

from src.db.models import User
from src.db.models.abstract_user import AbstractUser


async def text_start_answer(message: Message, user: User | AbstractUser) -> str:
    if user.is_super_admin:
        message = (f'Привет, {message.from_user.username}\n'
                   f'Для того, чтобы добавить админа введите команду /add_admin\n'
                   f'Для того, чтобы выйти из режима пользователя введите команду /user\n'
                   f'Для того, чтобы войти в режим админа введите команжу /admin')

    elif user.is_admin:
        message = (f'Привет, {message.from_user.username}\n'
                   f'Для того, чтобы выйти из режима пользователя введите команду /user\n'
                   f'Для того, чтобы войти в режим админа введите команжу /admin')
    else:
        message = f'Привет, {message.from_user.username}'

    return message
