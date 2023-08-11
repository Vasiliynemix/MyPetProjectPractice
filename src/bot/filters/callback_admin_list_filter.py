from aiogram.filters.callback_data import CallbackData


class CallBackAdminListFilter(CallbackData, prefix="list_admins"):
    admin_id: int
