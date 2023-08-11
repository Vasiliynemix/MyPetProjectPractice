import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.handlers import start_handler
from src.bot.handlers.admin_handlers import super_admin_commands, admin_handlers
from src.configurations import conf
from src.db.database import async_engine, create_session_maker


async def start_bot():
    bot: Bot = Bot(token=conf.bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(start_handler.router)
    dp.include_router(super_admin_commands.router)
    dp.include_router(admin_handlers.router)

    engine = async_engine(url=conf.db.build_url_for_db())
    session_maker = create_session_maker(engine=engine)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, session_maker=session_maker)


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging.logging_level)
    asyncio.run(start_bot())
