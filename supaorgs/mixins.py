from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .columns import IdColumn, ForeignKeyColumn


class TsMixin:
    created = Column(DateTime, server_default='now()', nullable=False, index=True)
    updated = Column(DateTime, server_onupdate='now()', nullable=False, index=True)


class IdMixin:
    id = IdColumn()


class BelongsToOrgMixin:
    organization_id = ForeignKeyColumn(ForeignKey('organizations.id'), nullable=False)


class OptionalOrgMixin:
    organization_id = ForeignKeyColumn(ForeignKey('organizations.id'), nullable=True)