from typing import List, Tuple

from sqlalchemy import Table, ForeignKey, Column, DateTime
from pg_rls.sqlalchemy import rls_for_table

from .base import Base
from .columns import ForeignKeyColumnNamed
schema = 'org'

def ManyToManyTable(name: str, *foreign_keys: Tuple[str, str], policies: list|None = None) -> Table:
    return rls_for_table(enabled=True, policies=policies)(Table(
        name,
        Base.metadata,
        *[
            ForeignKeyColumnNamed(fk[0], ForeignKey(fk[1]), primary_key=True) for fk in foreign_keys
        ],
        Column('created', DateTime, server_default='now()', nullable=False),
        Column('updated', DateTime, server_onupdate='now()', nullable=False),
        schema=schema
    ))