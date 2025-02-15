return exists(
    select key
    from current_resource_permissions(org_id, res_group_id)
    where key = permission
);