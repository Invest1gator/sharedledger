"""Migration for app1

Revision ID: 36c3080c78ac
Revises: 2afaaefffd35
Create Date: 2025-01-31 09:52:55.735625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36c3080c78ac'
down_revision: Union[str, None] = '2afaaefffd35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
