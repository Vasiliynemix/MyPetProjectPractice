from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_super_admin: Mapped[bool] = mapped_column(default=False)

