"""Careers portal job fields

Revision ID: 3913c92db66c
Revises: 4716a9c004b5
Create Date: 2026-07-12 18:34:51.544214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3913c92db66c'
down_revision: Union[str, Sequence[str], None] = '4716a9c004b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # -----------------------------
    # Jobs Table
    # -----------------------------

    op.add_column(
        "jobs",
        sa.Column("openings", sa.Integer(), nullable=True)
    )

    op.add_column(
        "jobs",
        sa.Column("salary_range", sa.String(length=100), nullable=True)
    )

    op.add_column(
        "jobs",
        sa.Column("work_mode", sa.String(length=50), nullable=True)
    )

    op.add_column(
        "jobs",
        sa.Column("nice_to_have_skills", sa.JSON(), nullable=True)
    )

    op.add_column(
        "jobs",
        sa.Column(
            "application_deadline",
            sa.DateTime(timezone=True),
            nullable=True
        )
    )

    op.add_column(
        "jobs",
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.true(),
            nullable=False
        )
    )

    op.alter_column(
        "jobs",
        "title",
        existing_type=sa.VARCHAR(length=100),
        type_=sa.String(length=150),
        existing_nullable=False
    )

    # -----------------------------
    # Users
    # -----------------------------

    op.alter_column(
        "users",
        "is_active",
        existing_type=sa.BOOLEAN(),
        nullable=False
    )


def downgrade() -> None:

    op.alter_column(
        "users",
        "is_active",
        existing_type=sa.BOOLEAN(),
        nullable=True
    )

    op.alter_column(
        "jobs",
        "title",
        existing_type=sa.String(length=150),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False
    )

    op.drop_column("jobs", "is_active")
    op.drop_column("jobs", "application_deadline")
    op.drop_column("jobs", "nice_to_have_skills")
    op.drop_column("jobs", "work_mode")
    op.drop_column("jobs", "salary_range")
    op.drop_column("jobs", "openings")
