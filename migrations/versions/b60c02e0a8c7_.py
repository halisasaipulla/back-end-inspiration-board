"""empty message

Revision ID: b60c02e0a8c7
Revises: 587505944eef
Create Date: 2021-07-01 14:27:06.398834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b60c02e0a8c7'
down_revision = '587505944eef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('color', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'color')
    # ### end Alembic commands ###
