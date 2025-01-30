select p.key
from permissions p
inner join resource_group_role_permissions rp on p.id = rp.permission_id
inner join resource_level_roles o on o.id = rp.role_id
inner join org_user_resource_level_roles our on o.id = our.role_id
where our.user_id = uid and our.organization_id = oid and our.resource_group_id = rg_id
union
select p.key
from permissions p
inner join resource_group_role_permissions rp on p.id = rp.permission_id
inner join resource_level_roles o on o.id = rp.role_id
inner join group_resource_roles gr on o.id = gr.role_id
inner join groups g on gr.group_id = g.id
inner join group_users gu on g.id = gu.group_id
where gu.user_id = uid and g.organization_id = oid and gr.resource_group_id = rg_id;