"""Renamed email as contact_email

Revision ID: 3c19130f8874
Revises: 791279dd0760
Create Date: 2025-03-08 10:21:51.920020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c19130f8874'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='contact_email')


def downgrade() -> None:
    op.alter_column('students', 'contact_email', new_column_name='email')
