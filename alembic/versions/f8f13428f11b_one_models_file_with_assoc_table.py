"""one-models-file-with_assoc_table

Revision ID: f8f13428f11b
Revises: 13cff3cafdf5
Create Date: 2024-12-11 08:10:50.070251+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8f13428f11b'
down_revision: Union[str, None] = '13cff3cafdf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###