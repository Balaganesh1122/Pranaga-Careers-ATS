"""Add professional career job fields

Revision ID: 9a5f8393969e
Revises: 3913c92db66c
Create Date: 2026-07-12 22:40:05.565375

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9a5f8393969e"
down_revision: Union[str, Sequence[str], None] = "3913c92db66c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # =====================================================
    # JOBS TABLE
    # =====================================================

    op.add_column(
        "jobs",
        sa.Column(
            "job_code",
            sa.String(length=30),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "team",
            sa.String(length=100),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "minimum_qualification",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "preferred_qualification",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "about_role",
            sa.Text(),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "benefits",
            sa.JSON(),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "selection_process",
            sa.JSON(),
            nullable=True,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "job_status",
            sa.String(length=30),
            server_default="Open",
            nullable=False,
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "posted_by",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.create_unique_constraint(
        "uq_jobs_job_code",
        "jobs",
        ["job_code"],
    )

    op.create_foreign_key(
        "fk_jobs_posted_by",
        "jobs",
        "users",
        ["posted_by"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_jobs_posted_by",
        "jobs",
        type_="foreignkey",
    )

    op.drop_constraint(
        "uq_jobs_job_code",
        "jobs",
        type_="unique",
    )

    op.drop_column("jobs", "posted_by")
    op.drop_column("jobs", "job_status")
    op.drop_column("jobs", "selection_process")
    op.drop_column("jobs", "benefits")
    op.drop_column("jobs", "about_role")
    op.drop_column("jobs", "preferred_qualification")
    op.drop_column("jobs", "minimum_qualification")
    op.drop_column("jobs", "team")
    op.drop_column("jobs", "job_code")