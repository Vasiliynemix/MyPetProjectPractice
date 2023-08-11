"""init

Revision ID: f256c6296d91
Revises: 
Create Date: 2023-08-11 23:00:17.212288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f256c6296d91'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('category_name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('category_name'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('is_admin', sa.Boolean(), nullable=False),
                    sa.Column('is_super_admin', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('telegram_id'),
                    sa.UniqueConstraint('telegram_id'),
                    sa.UniqueConstraint('username')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('category')
    # ### end Alembic commands ###