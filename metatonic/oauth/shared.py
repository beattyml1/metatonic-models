import enum


class AuthLevel(enum.Enum):
    USER = 'user'
    ORGANIZATION_USER = 'org_user'
    ORGANIZATION = 'organization'
    GLOBAL = 'global'
