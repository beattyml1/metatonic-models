import datetime

from pgalchemy import rls_base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime

Base = rls_base(declarative_base())


class CreateMixin:
    created = Column(DateTime, default=datetime.datetime.now())

class UpdateMixin:
    updated = Column(DateTime, onupdate=datetime.datetime.now())