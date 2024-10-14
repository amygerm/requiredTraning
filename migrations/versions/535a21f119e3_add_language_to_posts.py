"""add language to posts

Revision ID: 535a21f119e3
Revises: 687b31fe32ae
Create Date: 2024-10-14 12:05:43.434343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '535a21f119e3'
down_revision = '687b31fe32ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
