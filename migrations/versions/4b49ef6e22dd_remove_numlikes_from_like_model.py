"""remove numlikes from Like Model

Revision ID: 4b49ef6e22dd
Revises: 0de71cae9dde
Create Date: 2022-09-29 23:17:03.962367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b49ef6e22dd'
down_revision = '0de71cae9dde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('likes', 'num_likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('likes', sa.Column('num_likes', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
