"""Split full_name into first middle last name

Revision ID: 4716a9c004b5
Revises: 5386e92f3f0e
Create Date: 2026-07-12 16:52:44.336966
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "4716a9c004b5"
down_revision: Union[str, Sequence[str], None] = "5386e92f3f0e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

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
    """Downgrade schema."""

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