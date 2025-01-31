"""Merged heads

Revision ID: 2afaaefffd35
Revises: 27ac9786bb80, 985720b29861
Create Date: 2025-01-31 09:52:51.199334

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2afaaefffd35'
down_revision: Union[str, None] = ('27ac9786bb80', '985720b29861')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
