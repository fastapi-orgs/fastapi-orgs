import uuid
from typing import List, Optional, TypeVar

from pydantic import UUID4, BaseModel, Field


class BaseOrg(BaseModel):
    """Base Organization model."""

    id: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    is_active: bool = True
    parent: Optional[UUID4]
    children: Optional[List["BaseOrg"]] = []


class BaseOrgCreate(BaseModel):
    name: str
    is_active: Optional[bool] = True
    parent: Optional[UUID4]


class BaseOrgUpdate(BaseModel):
    id: UUID4
    name: Optional[str]
    is_active: Optional[bool]
    parent: Optional[UUID4]


class BaseOrgDB(BaseOrg):
    class Config:
        orm_mode = True


Org = TypeVar("Org", bound=BaseOrg)
OrgC = TypeVar("OrgC", bound=BaseOrgCreate)
OrgU = TypeVar("OrgU", bound=BaseOrgUpdate)
OrgD = TypeVar("OrgD", bound=BaseOrgDB)
