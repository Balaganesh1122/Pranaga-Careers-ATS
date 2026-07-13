"""Enhance interview module

Revision ID: 7966224dff95
Revises: 5c64185febe0
Create Date: 2026-07-14 00:14:43.101590
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "7966224dff95"
down_revision: Union[str, Sequence[str], None] = "5c64185febe0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Add new columns
    op.add_column(
        "interviews",
        sa.Column("interview_round", sa.String(length=50), nullable=False),
    )

    op.add_column(
        "interviews",
        sa.Column("interviewer_email", sa.String(length=150), nullable=True),
    )

    op.add_column(
        "interviews",
        sa.Column("feedback", sa.Text(), nullable=True),
    )

    op.add_column(
        "interviews",
        sa.Column("rating", sa.Float(), nullable=True),
    )

    # Modify existing columns
    op.alter_column(
        "interviews",
        "interview_type",
        existing_type=sa.VARCHAR(length=30),
        type_=sa.String(length=50),
        existing_nullable=False,
    )

    op.alter_column(
        "interviews",
        "status",
        existing_type=sa.VARCHAR(length=30),
        type_=sa.String(length=50),
        existing_nullable=True,
        nullable=False,
    )

    # Replace remarks -> feedback
    op.drop_column("interviews", "remarks")


def downgrade() -> None:
    """Downgrade schema."""

    op.add_column(
        "interviews",
        sa.Column("remarks", sa.Text(), nullable=True),
    )

    op.alter_column(
        "interviews",
        "status",
        existing_type=sa.String(length=50),
        type_=sa.VARCHAR(length=30),
        existing_nullable=False,
        nullable=True,
    )

    op.alter_column(
        "interviews",
        "interview_type",
        existing_type=sa.String(length=50),
        type_=sa.VARCHAR(length=30),
        existing_nullable=False,
    )

    op.drop_column("interviews", "rating")
    op.drop_column("interviews", "feedback")
    op.drop_column("interviews", "interviewer_email")
    op.drop_column("interviews", "interview_round")