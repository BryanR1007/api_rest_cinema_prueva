"""Create table

Revision ID: 2119202b49b7
Revises: 
Create Date: 2022-12-10 23:02:17.590241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2119202b49b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id_movie', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('url', sa.Text(), nullable=False),
    sa.Column('clasification', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id_movie')
    )
    op.create_table('tickets',
    sa.Column('id_ticket', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_ticket')
    )
    op.create_table('functions',
    sa.Column('id_function', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id_movie'], ),
    sa.PrimaryKeyConstraint('id_function')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('functions')
    op.drop_table('tickets')
    op.drop_table('movies')
    # ### end Alembic commands ###
