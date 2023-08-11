from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.orm import sessionmaker

from src.bot.filters.admin_filters import CallBackAdminListFilter
from src.db.queries import user_queries


async def get_list_admin(session_maker: sessionmaker) -> InlineKeyboardMarkup:
    list_admins_kb = InlineKeyboardBuilder()
    list_admins = await user_queries.get_list_admins(session_maker=session_maker)
    for admin in list_admins:
        list_admins_kb.button(text=admin.username,
                              callback_data=CallBackAdminListFilter(admin_id=admin.telegram_id))
    list_admins_kb.button(text='В начало',
                          callback_data='start_admin')
    list_admins_kb.adjust(1)
    return list_admins_kb.as_markup(resize_keyboard=True,
                                    one_time_keyboard=True)
