from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def start_admin_menu() -> InlineKeyboardMarkup:
    menu_admin = InlineKeyboardBuilder()
    menu_admin.button(text='Список категорий товаров', callback_data='list_categories')
    menu_admin.adjust(2)
    return menu_admin.as_markup(resize_keyboard=True,
                                one_time_keyboard=True)

