"""empty message

Revision ID: 22d420db1437
Revises: 
Create Date: 2022-10-18 19:36:44.110823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22d420db1437'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('module_title', sa.String(length=200), nullable=False),
    sa.Column('assessment_title', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('due_year', sa.Integer(), nullable=False),
    sa.Column('due_month', sa.Integer(), nullable=False),
    sa.Column('due_day', sa.Integer(), nullable=False),
    sa.Column('situation', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event')
    # ### end Alembic commands ###