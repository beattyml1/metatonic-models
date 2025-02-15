from uuid import UUID

from pgalchemy.functions import sql_function


class _WithKey:
    key: str

@sql_function(path='./functions/permissions_for_user.sql', schema='org')
def permissions_for_user(uid: UUID, oid: UUID) -> list[_WithKey]:
    pass

@sql_function(path='./functions/current_permissions.sql', schema='org')
def current_permissions(org_id: UUID) -> list[_WithKey]:
    pass

@sql_function(path='./functions/has_permission.sql', schema='org')
def has_permission(permission: str, org_id: UUID) -> list[_WithKey]:
    pass

@sql_function(path='./functions/resource_permissions_for_user.sql', schema='org')
def resource_permissions_for_user(uid: UUID, oid: UUID, rg_id: UUID) -> list[_WithKey]:
    pass

@sql_function(path='./functions/current_resource_permissions.sql', schema='org')
def current_resource_permissions(org_id: UUID, res_group_id: UUID) -> list[_WithKey]:
    pass

@sql_function(path='./functions/has_resource_permission.sql', schema='org')
def has_resource_permission(permission: str, org_id: UUID, res_group_id: UUID) -> list[_WithKey]:
    pass