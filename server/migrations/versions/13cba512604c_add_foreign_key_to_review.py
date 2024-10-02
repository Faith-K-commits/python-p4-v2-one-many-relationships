from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '13cba512604c'
down_revision = '9016b47750ee'
branch_labels = None
depends_on = None

def upgrade():
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)
    columns = [column['name'] for column in inspector.get_columns('reviews')]

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        if 'employee_id' not in columns:
            batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))

def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('employee_id')