"""Initial migration

Revision ID: 985720b29861
Revises: 
Create Date: 2025-01-31 06:09:49.787962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '985720b29861'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ledger_entries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('operation', sa.Enum('DAILY_REWARD', 'SIGNUP_CREDIT', 'CREDIT_SPEND', 'CREDIT_ADD', name='baseledgeroperation'), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('nonce', sa.String(), nullable=False),
    sa.Column('owner_id', sa.String(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nonce')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ledger_entries')
    # ### end Alembic commands ###
