from typing import List, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.db.models.category import Category


async def get_all_categories(session_maker: sessionmaker) -> Sequence[Category]:
    async with session_maker() as session:
        session: AsyncSession
        categories = await session.scalars(select(Category))
        return categories.all()
