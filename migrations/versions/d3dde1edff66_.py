"""empty message

Revision ID: d3dde1edff66
Revises: cc38d82b23cc
Create Date: 2023-12-17 02:57:44.340896

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3dde1edff66'
down_revision = 'cc38d82b23cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ElementsToProcess',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idBulk', sa.Integer(), nullable=True),
    sa.Column('retries', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('elements_to_process')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('elements_to_process',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('idBulk', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('retries', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('ElementsToProcess')
    # ### end Alembic commands ###