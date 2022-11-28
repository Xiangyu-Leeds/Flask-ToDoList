"""empty message

Revision ID: f90d43fd18cc
Revises: 9ce8cfdbf589
Create Date: 2022-11-06 23:25:04.093391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f90d43fd18cc'
down_revision = '9ce8cfdbf589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'event', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_column('event', 'author_id')
    # ### end Alembic commands ###