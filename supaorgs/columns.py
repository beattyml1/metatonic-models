import uuid

from sqlalchemy import Column, Text, UUID, ForeignKey, DateTime

users_table_name = 'auth.users'
schema = 'org'


def BizKeyColumn(unique=True, primary_key=False):
    return Column(Text, nullable=False, unique=unique, primary_key=primary_key)


def ForeignKeyColumn(fk: ForeignKey, *, nullable: bool = True, primary_key: bool = False):
    return Column(UUID, fk, nullable=nullable, index=True, primary_key=primary_key)


def ForeignKeyColumnNamed(name, fk: ForeignKey, *, nullable: bool = True, primary_key: bool = False):
    return Column(name, UUID, fk, nullable=nullable, index=True, primary_key=primary_key)


def UserIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(ForeignKey(f'{users_table_name}.id'), nullable=nullable, primary_key=primary_key)


def UserIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, ForeignKey(f'{users_table_name}.id'), nullable=nullable, primary_key=primary_key)


def OrganizationIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('organizations'), nullable=nullable, primary_key=primary_key)


def OrganizationIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('organizations'), nullable=nullable, primary_key=primary_key)


def OrgRoleIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('org_roles'), nullable=nullable, primary_key=primary_key)


def OrgRoleIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('org_roles'), nullable=nullable, primary_key=primary_key)


def ResourceRoleIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('resource_level_roles'), nullable=nullable, primary_key=primary_key)


def ResourceRoleIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('resource_level_roles'), nullable=nullable, primary_key=primary_key)


def ResourceGroupIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('resource_groups'), nullable=nullable, primary_key=primary_key)


def ResourceGroupIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('resource_groups'), nullable=nullable, primary_key=primary_key)


def ResourceTypeIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('resource_group_types'), nullable=nullable, primary_key=primary_key)


def ResourceTypeIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('resource_group_types'), nullable=nullable, primary_key=primary_key)


def GroupIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('groups'), nullable=nullable, primary_key=primary_key)


def GroupIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('groups'), nullable=nullable, primary_key=primary_key)


def PermissionIdColumn(*, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumn(FkTo('permissions'), nullable=nullable, primary_key=primary_key)


def PermissionIdColumnNamed(name, *, nullable: bool = True, primary_key: bool = False):
    return ForeignKeyColumnNamed(name, FkTo('permissions'), nullable=nullable, primary_key=primary_key)


def FkTo(table_name):
    return ForeignKey(f'{schema}.{table_name}.id')


def IdColumn():
    return Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False, server_default='gen_random_uuid()')


def CreateTsColumn(index=True):
    return Column(DateTime, server_default='now()', nullable=False, index=index)


def UpdateTsColumn(index=True):
    return Column(DateTime, server_onupdate='now()', nullable=False, index=index)