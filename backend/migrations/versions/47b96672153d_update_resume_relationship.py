"""Update resume relationship

Revision ID: 47b96672153d
Revises: e273c93a115f
Create Date: 2026-07-13 20:58:50.728576
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "47b96672153d"
down_revision: Union[str, Sequence[str], None] = "e273c93a115f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column(
        "resume_data",
        sa.Column("candidate_id", sa.Integer(), nullable=True),
    )

    op.add_column(
        "resume_data",
        sa.Column("extracted_name", sa.String(length=150), nullable=True),
    )

    op.add_column(
        "resume_data",
        sa.Column("extracted_email", sa.String(length=150), nullable=True),
    )

    op.add_column(
        "resume_data",
        sa.Column("extracted_phone", sa.String(length=30), nullable=True),
    )

    op.add_column(
        "resume_data",
        sa.Column("extracted_skills", sa.Text(), nullable=True),
    )

    op.add_column(
        "resume_data",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
    )

    op.drop_constraint(
        "resume_data_application_id_key",
        "resume_data",
        type_="unique",
    )

    op.drop_constraint(
        "resume_data_application_id_fkey",
        "resume_data",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "resume_data_candidate_id_fkey",
        "resume_data",
        "candidates",
        ["candidate_id"],
        ["id"],
    )

    op.create_unique_constraint(
        "resume_data_candidate_id_key",
        "resume_data",
        ["candidate_id"],
    )

    op.drop_column("resume_data", "application_id")


def downgrade() -> None:

    op.add_column(
        "resume_data",
        sa.Column("application_id", sa.Integer(), nullable=False),
    )

    op.drop_constraint(
        "resume_data_candidate_id_key",
        "resume_data",
        type_="unique",
    )

    op.drop_constraint(
        "resume_data_candidate_id_fkey",
        "resume_data",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "resume_data_application_id_fkey",
        "resume_data",
        "applications",
        ["application_id"],
        ["id"],
    )

    op.create_unique_constraint(
        "resume_data_application_id_key",
        "resume_data",
        ["application_id"],
    )

    op.drop_column("resume_data", "updated_at")
    op.drop_column("resume_data", "extracted_skills")
    op.drop_column("resume_data", "extracted_phone")
    op.drop_column("resume_data", "extracted_email")
    op.drop_column("resume_data", "extracted_name")
    op.drop_column("resume_data", "candidate_id")