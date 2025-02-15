from typing import Type

from sqlalchemy import BinaryExpression, Table
from sqlalchemy.orm import DeclarativeBase


def scope(
        on: Type[DeclarativeBase] | Table,
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