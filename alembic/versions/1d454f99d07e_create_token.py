"""create token

Revision ID: 1d454f99d07e
Revises: 869a9af6fd76
Create Date: 2023-11-14 01:05:36.012584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d454f99d07e"
down_revision: Union[str, None] = "869a9af6fd76"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tokens",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("access_token", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_tokens_access_token"), "tokens", ["access_token"], unique=True
    )
    op.create_index(op.f("ix_tokens_id"), "tokens", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tokens_id"), table_name="tokens")
    op.drop_index(op.f("ix_tokens_access_token"), table_name="tokens")
    op.drop_table("tokens")
    # ### end Alembic commands ###