from typing import Type

import sqlalchemy
from pgalchemy import Policy, PolicyType, PolicyCommands
from sqlalchemy import Table, BinaryExpression
from sqlalchemy.orm import DeclarativeBase


def permissions(
        on: Type[DeclarativeBase] | Table,
        org: BinaryExpression,
        select: str,
        insert: str | None = None,
        update: str | None = None,
        delete: str | None = None,
        write: str | None = None,
        prefix: str | None = None,
):
    insert = insert or write
    update = update or write
    delete = delete or write
    # TODO: setup permissions and revoke update on org_expression

class HasPermissionPolicy(Policy):
    def __init__(
            self,
            on: Type[DeclarativeBase] | Table,
            name: str,
            permission: str,
            org_expression: BinaryExpression,
            as_: PolicyType = PolicyType.PERMISSIVE,
            for_: PolicyCommands = PolicyCommands.ALL
    ):
        super().__init__(
            on, name, as_, for_,
            sqlalchemy.func.has_permission(permission, org_expression),
            sqlalchemy.func.has_permission(permission, org_expression)
        )


class HasResourcePermissionPolicy(Policy):
    def __init__(
            self,
            on: Type[DeclarativeBase] | Table,
            name: str,
            permission: str,
            org_expression: BinaryExpression,
            resource_expression: BinaryExpression,
            as_: PolicyType = PolicyType.PERMISSIVE,
            for_: PolicyCommands = PolicyCommands.ALL
    ):
        super().__init__(
            on, name, as_, for_,
            sqlalchemy.func.has_permission(permission, org_expression, resource_expression),
            sqlalchemy.func.has_permission(permission, org_expression, resource_expression)
        )