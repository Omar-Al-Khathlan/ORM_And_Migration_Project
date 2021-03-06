"""Second

Revision ID: de959efb119e
Revises: 2b1222ba4573
Create Date: 2022-06-02 12:17:47.598961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de959efb119e'
down_revision = '2b1222ba4573'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('academic_hours', sa.Integer(), nullable=True),
    sa.Column('actual_hours', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('gpa', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('extra_data', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['course.id'], ),
    sa.ForeignKeyConstraint(['sid'], ['student.id'], ),
    sa.PrimaryKeyConstraint('sid', 'cid')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['course.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher')
    op.drop_table('association')
    op.drop_table('student')
    op.drop_table('course')
    # ### end Alembic commands ###
