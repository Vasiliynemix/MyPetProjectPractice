from aiogram.filters.callback_data import CallbackData


class CallBackCategoryListFilter(CallbackData, prefix="category"):
    category: str
