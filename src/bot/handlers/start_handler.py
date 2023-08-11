from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker

from src.bot.fsm_models.fsm_main import FSMMainUser, FSMMainAdmin
from src.bot.lexicon_ru.start_answer import text_start_answer
from src.db.models import User
from src.db.queries import user_queries

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext, session_maker: sessionmaker):
    user: User = await user_queries.get_user_by_id(message, session_maker)
    if user is None:
        await user_queries.set_user(message, session_maker)
    if user.is_admin:
        await state.set_state(FSMMainAdmin.start)
        await message.answer(
            await text_start_answer(message=message, user=user)
        )
    else:
        await state.set_state(FSMMainUser.start)
        await message.answer(
            await text_start_answer(message=message, user=user)
        )
