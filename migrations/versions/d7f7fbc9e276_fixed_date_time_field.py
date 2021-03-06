"""fixed date time field

Revision ID: d7f7fbc9e276
Revises: 744cfe459da9
Create Date: 2019-11-06 15:34:52.247518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7f7fbc9e276'
down_revision = '744cfe459da9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_event_event_date'), 'event', ['event_date'], unique=False)
    op.create_index(op.f('ix_event_event_manager'), 'event', ['event_manager'], unique=False)
    op.create_index(op.f('ix_event_event_type'), 'event', ['event_type'], unique=False)
    op.create_index(op.f('ix_event_other_notes'), 'event', ['other_notes'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_other_notes'), table_name='event')
    op.drop_index(op.f('ix_event_event_type'), table_name='event')
    op.drop_index(op.f('ix_event_event_manager'), table_name='event')
    op.drop_index(op.f('ix_event_event_date'), table_name='event')
    # ### end Alembic commands ###
