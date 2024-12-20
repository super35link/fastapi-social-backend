"""fix_models

Revision ID: feb2b113f495
Revises: 3fc0dd8124bd
Create Date: 2024-12-11 07:37:11.111088+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'feb2b113f495'
down_revision: Union[str, None] = '3fc0dd8124bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hashtags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('usage_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hashtags_id'), 'hashtags', ['id'], unique=False)
    op.create_index(op.f('ix_hashtags_tag'), 'hashtags', ['tag'], unique=True)
    op.create_table('threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_collaborative', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_threads_id'), 'threads', ['id'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=500), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('thread_id', sa.Integer(), nullable=True),
    sa.Column('position_in_thread', sa.Integer(), nullable=True),
    sa.Column('reply_to_id', sa.Integer(), nullable=True),
    sa.Column('content_vector', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('like_count', sa.Integer(), nullable=True),
    sa.Column('repost_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['reply_to_id'], ['posts.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.create_table('post_hashtags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('hashtag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hashtag_id'], ['hashtags.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE')
    )
    op.create_table('post_mentions',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_mentions')
    op.drop_table('post_hashtags')
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_threads_id'), table_name='threads')
    op.drop_table('threads')
    op.drop_index(op.f('ix_hashtags_tag'), table_name='hashtags')
    op.drop_index(op.f('ix_hashtags_id'), table_name='hashtags')
    op.drop_table('hashtags')
    # ### end Alembic commands ###
