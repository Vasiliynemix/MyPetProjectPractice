from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker

from src.bot.fsm_models.fsm_main import FSMMainAdmin
from src.bot.keyboards.super_admin_kb import get_list_admin
from src.bot.middlewares.Is_super_admin_middlewares import IsSuperAdmin
from src.db.queries import user_queries

router = Router()

router.message.middleware(IsSuperAdmin())
router.callback_query.middleware(IsSuperAdmin())


@router.message(Command(commands=['list_admins']))
async def list_admins(message: Message, session_maker: sessionmaker):
    await message.answer(
        'Список админов\nДля того, чтобы удалить админа нажмите на него',
        reply_markup=await get_list_admin(session_maker=session_maker)
    )


@router.message(Command(commands=['add_admin']))
async def add_new_admin(message: Message, state: FSMContext):
    await state.set_state(FSMMainAdmin.add_admin)
    await message.answer('Введите id или username пользователя, кому хотите дать права админа')


@router.message(FSMMainAdmin.add_admin, F.text.isdigit())
async def get_id_new_admin(message: Message, state: FSMContext, session_maker: sessionmaker):
    user = await user_queries.add_admin_by_id(message=message, session_maker=session_maker)
    if user:
        await message.answer(
            f'{user.username} добавлен в список админов\nЧтобы удалить админа из списка нажмите на его username',
            reply_markup=await get_list_admin(session_maker=session_maker)
        )
    else:
        await state.set_state(FSMMainAdmin.add_admin)
        await message.answer(f'пользователь {message.text} не найден, введите корректные данные')


@router.message(FSMMainAdmin.add_admin)
async def get_username_new_admin(message: Message, state: FSMContext, session_maker: sessionmaker):
    user = await user_queries.add_admin_by_username(message=message, session_maker=session_maker)
    if user:
        await message.answer(
            f'{user.username} добавлен в список админов\nЧтобы удалить админа из списка нажмите на его username',
            reply_markup=await get_list_admin(session_maker=session_maker)
        )
    else:
        await state.set_state(FSMMainAdmin.add_admin)
        await message.answer(f'пользователь {message.text} не найден, введите корректные данные')


@router.callback_query(lambda c: c.data == 'start_admin')
async def remove_admin(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.set_state(FSMMainAdmin.start)
    await call.message.edit_text('Меню')


@router.callback_query(lambda c: c.data == F.admin_id)
async def remove_admin(call: CallbackQuery, session_maker: sessionmaker):
    await call.answer()
    user = await user_queries.remove_admin(call=call, session_maker=session_maker)
    await call.message.edit_text(
        (f'{user.username} удален из списка админов\n'
         f'Чтобы удалить админа из списка нажмите на его username\n'
         f'Список админов'),
        reply_markup=await get_list_admin(session_maker=session_maker)
    )
