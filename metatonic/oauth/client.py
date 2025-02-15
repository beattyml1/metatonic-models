import uuid

from sqlalchemy import Column, Text, UUID, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from .shared import AuthLevel


class OAuth2Server:
    id = Column(UUID, primary_key=True, insert_default=uuid.uuid4)
    key = Column(Text, nullable=False)
    label = Column(Text, nullable=False)
    client_id = Column(Text, nullable=False)
    client_secret = Column(Text, nullable=False)
    authorization_endpoint = Column(Text, nullable=False)
    token_endpoint = Column(Text, nullable=False)
    redirect_uri = Column(Text, nullable=False)
    required_scopes = Column(ARRAY(Text), nullable=False)
    optional_scopes = Column(ARRAY(Text), nullable=False)
    levels = Column(ARRAY(Enum(AuthLevel)), nullable=False)


class OAuthConnection:
    id = Column(UUID, primary_key=True, insert_default=uuid.uuid4)
    level = Column(Enum(AuthLevel), default=AuthLevel.ORGANIZATION_USER)
    user_id = Column(UUID, ForeignKey('user.id', ondelete='CASCADE'))
    organization_id = Column(UUID, ForeignKey('org.organizations.id', ondelete='CASCADE'), nullable=True)
    user = relationship('User')
    organization = relationship('Organization')
