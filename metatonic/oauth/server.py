import enum
import time
from authlib.integrations.sqla_oauth2 import (
    OAuth2ClientMixin,
    OAuth2AuthorizationCodeMixin,
    OAuth2TokenMixin,
)
from sqlalchemy import Column, Integer, ForeignKey, relationship, UUID, Enum
from sqlalchemy.dialects.postgresql import ARRAY

from metatonic.base import Base, CreateMixin, UpdateMixin
from .shared import AuthLevel


class OAuth2Client(Base, OAuth2ClientMixin, CreateMixin, UpdateMixin):
    __tablename__ = 'oauth2_client'

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.id', ondelete='CASCADE'))
    organization_id = Column(UUID, ForeignKey('org.organizations.id', ondelete='CASCADE'), nullable=True)
    levels = Column(ARRAY(Enum(AuthLevel)), default=AuthLevel.ORGANIZATION_USER)
    user = relationship('User')


class OAuth2AuthorizationCode(Base, OAuth2AuthorizationCodeMixin, CreateMixin, UpdateMixin):
    __tablename__ = 'oauth2_code'

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.id', ondelete='CASCADE'))
    level = Column(Enum(AuthLevel), default=AuthLevel.ORGANIZATION_USER)
    organization_id = Column(UUID, ForeignKey('org.organizations.id', ondelete='CASCADE'), nullable=True)
    user = relationship('User')

class OAuth2Token(Base, OAuth2TokenMixin, CreateMixin, UpdateMixin):
    __tablename__ = 'oauth2_token'

    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.id', ondelete='CASCADE'))
    level = Column(Enum(AuthLevel), default=AuthLevel.ORGANIZATION_USER)
    organization_id = Column(UUID, ForeignKey('org.organizations.id', ondelete='CASCADE'), nullable=True)
    user = relationship('User')
    organization = relationship('Organization')

    def is_refresh_token_active(self):
        if self.revoked:
            return False
        expires_at = self.issued_at + self.expires_in * 2
        return expires_at >= time.time()
