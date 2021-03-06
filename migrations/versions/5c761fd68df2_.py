"""empty message

Revision ID: 5c761fd68df2
Revises: 8641cbd3a9de
Create Date: 2020-11-20 03:38:17.475198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c761fd68df2'
down_revision = '8641cbd3a9de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
