from sqlalchemy import Column, ForeignKey, Text, Table
from sqlalchemy.orm import relationship, declarative_base
from pgalchemy.rls import rls_base

from .base import Base
from .columns import BizKeyColumn, ForeignKeyColumn, ForeignKeyColumnNamed, FkTo
from .helpers import ManyToManyTable
from .mixins import TsMixin, IdMixin, BelongsToOrgMixin, OptionalOrgMixin

users_table_name = 'auth.users'
schema = 'org'

base_table_args = {'schema': schema}


class Organization(Base, TsMixin, IdMixin):
    __tablename__ = 'organizations'
    name = Column(Text, nullable=False)
    owner_id = ForeignKeyColumn(ForeignKey(f'{users_table_name}.id'), nullable=False)
    owner = relationship('User')
    roles = relationship('OrgRole', back_populates='organization')
    resource_roles = relationship('ResourceLevelRoles', back_populates='organization')
    users = relationship('OrgUser', back_populates='organization')
    resource_groups = relationship('ResourceGroup', back_populates='organization')
    groups = relationship('Group', back_populates='organization')


class OrgRole(Base, TsMixin, IdMixin, BelongsToOrgMixin):
    __tablename__ = 'org_roles'
    label = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    organization = relationship('Organization', back_populates='roles')
    permissions = relationship('Permission', secondary='org_role_permissions')


class Permission(Base, TsMixin, IdMixin, OptionalOrgMixin):
    __tablename__ = 'permissions'
    key = BizKeyColumn()
    label = Column(Text, nullable=False)
    description = Column(Text, nullable=True)


class ResourceGroupType(Base, TsMixin, IdMixin):
    __tablename__ = 'resource_group_types'
    key = BizKeyColumn()
    label = Column(Text, nullable=False)
    description = Column(Text, nullable=True)


class ResourceGroup(Base, TsMixin, IdMixin, BelongsToOrgMixin):
    __tablename__ = 'resource_groups'
    type_id = ForeignKeyColumn(ForeignKey('resource_types.id'), nullable=False)
    label = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    type = relationship('ResourceGroupType')
    organization = relationship('Organization', back_populates='resource_groups')


class ResourceLevelRole(Base, TsMixin, IdMixin, BelongsToOrgMixin):
    __tablename__ = 'resource_level_roles'
    label = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    organization = relationship('Organization', back_populates='resource_roles')
    users = relationship('OrgUser', secondary='org_user_resource_level_roles')
    groups = relationship('Group', secondary='group_resource_level_roles')


class Group(Base, TsMixin, IdMixin, BelongsToOrgMixin):
    __tablename__ = 'groups'
    label = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    organization = relationship('Organization', back_populates='groups')
    users = relationship('OrgUser', secondary='group_users')
    roles = relationship('OrgRole', secondary='org_roles')
    resource_roles = relationship('ResourceLevelRole', secondary='resource_group_roles')
