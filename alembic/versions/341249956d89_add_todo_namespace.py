"""add todo namespace

Revision ID: 341249956d89
Revises: fb0890cc55c9
Create Date: 2022-01-24 16:22:11.857875

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "341249956d89"
down_revision = "fb0890cc55c9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("todos", sa.Column("namespace", sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("todos", "namespace")
    # ### end Alembic commands ###
