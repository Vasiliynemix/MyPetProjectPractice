from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from sqlalchemy.orm import sessionmaker

from src.bot.filters.user_filters import CallBackCategoryListFilter
from src.bot.fsm_models.fsm_main import FSMMainAdmin, FSMMainUser
from src.bot.keyboards import admin_kb, user_kb
from src.bot.lexicon_ru.start_answer import text_start_answer
from src.bot.middlewares.is_admin_middleware import IsAdmin
from src.db.models.abstract_user import AbstractUser

router = Router()

router.message.middleware(IsAdmin())
router.callback_query.middleware(IsAdmin())


@router.message(Command(commands=['user']))
async def start_user_mode(message: Message, state: FSMContext):
    user = AbstractUser()
    await state.set_state(FSMMainUser.start)
    await message.answer(
        await text_start_answer(message=message, user=user)
    )


@router.message(Command(commands=['admin']))
async def start_admin_mode(message: Message, state: FSMContext):
    await state.set_state(FSMMainAdmin.start)
    await message.answer(
        'Вы в режиме админа\nВыберите из списка ниже, что хотите сделать.',
        reply_markup=await admin_kb.start_admin_menu()
    )


@router.callback_query(FSMMainAdmin.start, lambda c: c.data == 'list_categories')
async def get_list_of_categories(call: CallbackQuery, state: FSMContext, session_maker: sessionmaker):
    await state.set_state(FSMMainAdmin.list_categories)
    await call.answer()
    await call.message.edit_text(
        'Список доступных категорий товаров',
        reply_markup=await user_kb.list_categories(session_maker=session_maker)
    )


# @router.callback_query(FSMMainAdmin.list_categories, CallBackCategoryListFilter.filter())
# async def test(call: CallbackQuery, state: FSMContext, session_maker: sessionmaker):
#     await state.set_state(FSMMainAdmin.list_categories)
#     await call.answer()
#     await call.message.answer(call.data)
