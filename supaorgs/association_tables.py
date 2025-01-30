from pg_rls_orgs.helpers import ManyToManyTable
schema = 'org'
users_table_name = 'auth.users'

group_resource_roles = ManyToManyTable(
    'group_resource_roles',
    ('group_id', f'{schema}.groups.id'),
    ('resource_group_id', f'{schema}.resource_groups.id'),
    ('role_id', f'{schema}.resource_level_roles.id'),
    policies=[
    ]
)

group_roles = ManyToManyTable(
    'group_roles',
    ('group_id', f'{schema}.groups.id'),
    ('role_id', f'{schema}.org_roles.id'),
    policies=[
    ]
)

group_users = ManyToManyTable(
    'group_users',
    ('group_id', f'{schema}.groups.id'),
    ('user_id', f'{users_table_name}.id'),
    policies=[
    ]
)

resource_group_role_permissions = ManyToManyTable(
    'resource_group_role_permissions',
    ('permission_id', f'{schema}.permissions.id'),
    ('role_id', f'{schema}.resource_level_roles.id'),
    policies=[
    ]
)

org_user_resource_level_roles = ManyToManyTable(
    'org_user_resource_level_roles',
    ('organization_id', f'{schema}.organizations.id'),
    ('resource_group_id', f'{schema}.resource_groups.id'),
    ('user_id', f'{users_table_name}.id'),
    ('role_id', f'{schema}.resource_level_roles.id'),
    policies=[
    ]
)


role_permission = ManyToManyTable(
    'role_permissions',
    ('permission_id', f'{schema}.permissions.id'),
    ('role_id', f'{schema}.roles.id'),
    policies=[

    ]
)

org_users = ManyToManyTable(
    'org_users',
    ('organization_id', f'{schema}.organizations.id'),
    ('user_id', f'{users_table_name}.id'),
    policies=[
    ]
)
org_user_roles = ManyToManyTable(
    'org_user_roles',
    ('organization_id', f'{schema}.organizations.id'),
    ('role_id', f'{schema}.org_roles.id'),
    ('user_id', f'{users_table_name}.id'),
    policies=[
    ]
)