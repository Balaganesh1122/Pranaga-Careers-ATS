"""Update email logs

Revision ID: e44b3d002220
Revises: 7966224dff95
Create Date: 2026-07-18 16:25:51.126180

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e44b3d002220"
down_revision: Union[str, Sequence[str], None] = "7966224dff95"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "email_logs",
        sa.Column(
            "email_type",
            sa.String(length=100),
            nullable=False,
            server_default="Application",
        ),
    )

    op.add_column(
        "email_logs",
        sa.Column(
            "error_message",
            sa.Text(),
            nullable=True,
        ),
    )

    op.alter_column(
        "email_logs",
        "recipient",
        existing_type=sa.VARCHAR(length=150),
        nullable=False,
    )

    op.alter_column(
        "email_logs",
        "subject",
        existing_type=sa.VARCHAR(length=255),
        nullable=False,
    )

    op.alter_column(
        "email_logs",
        "status",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )

    op.create_index(
        "ix_email_logs_id",
        "email_logs",
        ["id"],
        unique=False,
    )

    op.alter_column(
        "email_logs",
        "email_type",
        server_default=None,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_email_logs_id",
        table_name="email_logs",
    )

    op.alter_column(
        "email_logs",
        "status",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )

    op.alter_column(
        "email_logs",
        "subject",
        existing_type=sa.VARCHAR(length=255),
        nullable=True,
    )

    op.alter_column(
        "email_logs",
        "recipient",
        existing_type=sa.VARCHAR(length=150),
        nullable=True,
    )

    op.drop_column(
        "email_logs",
        "error_message",
    )

    op.drop_column(
        "email_logs",
        "email_type",
    )