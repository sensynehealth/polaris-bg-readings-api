"""empty message

Revision ID: 254b34815457
Revises: 03d69ee85e1d
Create Date: 2018-01-05 13:11:50.923151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254b34815457'
down_revision = 'aec5b45a6424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('reading_uuid', 'reading', ['uuid'], unique=True)
    op.create_index('note_uuid', 'note', ['uuid'], unique=True)
    op.create_index('dose_uuid', 'dose', ['uuid'], unique=True)
    op.create_index('prandial_tag_uuid', 'prandial_tag', ['uuid'], unique=True)
    op.create_index('reading_metadata_uuid', 'reading_metadata', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('reading_uuid', table_name='reading')
    op.drop_index('note_uuid', table_name='note')
    op.drop_index('dose_uuid', table_name='dose')
    op.drop_index('prandial_tag_uuid', table_name='prandial_tag')
    op.drop_index('reading_metadata_uuid', table_name='reading_metadata')
    # ### end Alembic commands ###
