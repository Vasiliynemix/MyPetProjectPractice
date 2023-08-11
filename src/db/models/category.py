from sqlalchemy.orm import Mapped, mapped_column

from src.db.models import Base


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(autoincrement=True, unique=True, primary_key=True)

    category_name: Mapped[str] = mapped_column(unique=True)
