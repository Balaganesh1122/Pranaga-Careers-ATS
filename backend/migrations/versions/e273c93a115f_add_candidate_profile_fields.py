"""Add candidate profile fields

Revision ID: e273c93a115f
Revises: 9a5f8393969e
Create Date: 2026-07-12 22:55:42.840419
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e273c93a115f"
down_revision: Union[str, Sequence[str], None] = "9a5f8393969e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "candidates",
        sa.Column("country", sa.String(length=100), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("state", sa.String(length=100), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("city", sa.String(length=100), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("highest_education", sa.String(length=150), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("years_of_experience", sa.Float(), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("current_company", sa.String(length=150), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("current_designation", sa.String(length=150), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("expected_ctc", sa.Float(), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("current_ctc", sa.Float(), nullable=True),
    )

    op.add_column(
        "candidates",
        sa.Column("notice_period", sa.String(length=100), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column("candidates", "notice_period")
    op.drop_column("candidates", "current_ctc")
    op.drop_column("candidates", "expected_ctc")
    op.drop_column("candidates", "current_designation")
    op.drop_column("candidates", "current_company")
    op.drop_column("candidates", "years_of_experience")
    op.drop_column("candidates", "highest_education")
    op.drop_column("candidates", "city")
    op.drop_column("candidates", "state")
    op.drop_column("candidates", "country")