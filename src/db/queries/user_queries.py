import os
from typing import List

from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.configurations import conf
from src.db.models import User


async def set_user(message: Message, session_maker: sessionmaker):
    async with session_maker() as session:
        session: AsyncSession
        await session.execute(select(User))
        if message.from_user.id == conf.super_admin:
            user = User(telegram_id=message.from_user.id,
                        is_admin=True,
                        is_super_admin=True,
                        username=message.from_user.username)
        else:
            user = User(telegram_id=message.from_user.id)
        await session.merge(user)
        await session.commit()
        return user


async def get_user_by_id(message: Message, session_maker: sessionmaker):
    async with session_maker() as session:
        query = await session.scalar(select(User).where(User.telegram_id == message.from_user.id))
        return query


async def add_admin_by_id(message: Message, session_maker: sessionmaker) -> User | bool:
    async with session_maker() as session:
        user = await session.scalar(select(User).where(User.telegram_id == int(message.text)))
        if user is None:
            return False
        user.is_admin = True
        await session.merge(user)
        await session.commit()
        return user


async def add_admin_by_username(message: Message, session_maker: sessionmaker) -> User | bool:
    async with session_maker() as session:
        user = await session.scalar(select(User).where(User.username == message.text))
        if user is None:
            return False
        user.is_admin = True
        await session.merge(user)
        await session.commit()
        return user


async def get_list_admins(session_maker: sessionmaker) -> List[User]:
    async with session_maker() as session:
        users = await session.scalars(select(User).where(User.is_admin))
        return users


async def remove_admin(call: CallbackQuery, session_maker: sessionmaker, bot: Bot):
    async with session_maker() as session:
        user = await session.scalar(select(User).where(User.telegram_id == int(call.data[12:])))
        if user.telegram_id == int(os.getenv('SUPER_ADMIN')):
            await call.message.answer('Вы не можете удалить сами себя из списка админа, извините')
            return user
        user.is_admin = False
        await session.merge(user)
        await session.commit()
        await bot.send_message(call.data[12:], 'Вы больше не админ!')
        return user
