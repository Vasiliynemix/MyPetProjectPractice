from aiogram.filters import Filter
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message


class CallBackAdminListFilter(CallbackData, prefix="list_admins"):
    admin_id: int
