"""Split full name into first middle last

Revision ID: 5c64185febe0
Revises: 47b96672153d
Create Date: 2026-07-13 21:27:41.861779
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5c64185febe0"
down_revision: Union[str, Sequence[str], None] = "47b96672153d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "candidates",
        sa.Column("first_name", sa.String(length=100), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("middle_name", sa.String(length=100), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("last_name", sa.String(length=100), nullable=True),
    )

    op.execute("""
        UPDATE candidates
        SET first_name = full_name
    """)

    op.drop_column("candidates", "full_name")


def downgrade() -> None:

    op.add_column(
        "candidates",
        sa.Column("full_name", sa.String(length=150), nullable=True),
    )

    op.execute("""
        UPDATE candidates
        SET full_name = first_name
    """)

    op.drop_column("candidates", "last_name")
    op.drop_column("candidates", "middle_name")
    op.drop_column("candidates", "first_name")