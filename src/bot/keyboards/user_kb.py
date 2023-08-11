from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.orm import sessionmaker

from src.bot.filters.user_filters import CallBackCategoryListFilter
from src.db.queries import categiry_queries


async def list_categories(session_maker: sessionmaker):
    list_category_kb = InlineKeyboardBuilder()
    categories = await categiry_queries.get_all_categories(session_maker=session_maker)
    for category in categories:
        list_category_kb.button(text=category.category_name,
                                callback_data=CallBackCategoryListFilter(category=category.category_name))
    list_category_kb.adjust(2)
    return list_category_kb.as_markup(resize_keyboard=True,
                                      one_time_keyboard=True)
