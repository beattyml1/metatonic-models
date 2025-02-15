from pgalchemy import rls_base
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

_base = declarative_base(metadata=MetaData(schema='org'))
Base = rls_base(_base)