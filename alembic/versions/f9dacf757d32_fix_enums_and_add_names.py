"""Fix enums and add names

Revision ID: f9dacf757d32
Revises: 
Create Date: 2024-12-19 22:43:30.107977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9dacf757d32'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classrooms',
    sa.Column('classroom_id', sa.Integer(), nullable=False),
    sa.Column('classroom_number', sa.Integer(), nullable=False),
    sa.Column('classroom_type', sa.Enum('lab', 'normal', name='classroom_type_enum'), nullable=False),
    sa.Column('classroom_nfccode', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('classroom_id'),
    sa.UniqueConstraint('classroom_nfccode')
    )
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(), nullable=False),
    sa.Column('subject_description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_email', sa.String(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('user_lastname', sa.String(), nullable=False),
    sa.Column('user_img', sa.String(), nullable=True),
    sa.Column('user_role', sa.Enum('teacher', 'admin', name='user_role_enum'), nullable=False),
    sa.Column('user_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('user_email')
    )
    op.create_table('classes',
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('class_day', sa.Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', name='class_day_enum'), nullable=False),
    sa.Column('class_course', sa.String(), nullable=False),
    sa.Column('class_hour_start', sa.Time(), nullable=False),
    sa.Column('class_hour_end', sa.Time(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('classroom_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.classroom_id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('class_id')
    )
    op.create_table('reports',
    sa.Column('report_id', sa.Integer(), nullable=False),
    sa.Column('report_datetime', sa.DateTime(), nullable=False),
    sa.Column('classroom_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.classroom_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('report_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reports')
    op.drop_table('classes')
    op.drop_table('users')
    op.drop_table('subjects')
    op.drop_table('classrooms')
    # ### end Alembic commands ###
