"""empty message

Revision ID: 1b7f325e8f0e
Revises: 892f56376a92
Create Date: 2018-04-25 13:32:19.433139

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1b7f325e8f0e'
down_revision = '892f56376a92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patient', sa.Column(
        'suppress_reading_alerts_from_tz', sa.Integer(), nullable=True))
    op.add_column('patient', sa.Column(
        'suppress_reading_alerts_until_tz', sa.Integer(), nullable=True))
    op.alter_column('patient', 'suppress_reading_alerts_from',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patient', 'suppress_reading_alerts_from',
                    existing_type=postgresql.TIMESTAMP(),
                    nullable=True)
    op.drop_column('patient', 'suppress_reading_alerts_until_tz')
    op.drop_column('patient', 'suppress_reading_alerts_from_tz')
    # ### end Alembic commands ###