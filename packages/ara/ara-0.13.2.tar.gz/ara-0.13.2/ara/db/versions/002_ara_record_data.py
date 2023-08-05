#   Copyright 2017 Red Hat, Inc. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

"""ara_record data

Revision ID: e8e78fd08bf2
Revises: da9459a1f71c
Create Date: 2016-11-01 18:02:38.685998

"""
# flake8: noqa
# revision identifiers, used by Alembic.
revision = 'e8e78fd08bf2'
down_revision = 'da9459a1f71c'

from ara import models
from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('data',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('playbook_id', sa.String(length=36), nullable=True),
    sa.Column('key', sa.String(length=255), nullable=True),
    sa.Column('value', models.CompressedData((2 ** 32) - 1), nullable=True),
    sa.ForeignKeyConstraint(['playbook_id'], ['playbooks.id'], ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('playbook_id', 'key')
    )
    ### end Alembic commands ###


def downgrade():
    op.drop_table('data')
    ### end Alembic commands ###
