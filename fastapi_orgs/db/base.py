from typing import Generic, Optional, Type

from pydantic import UUID4

from fastapi_orgs.models import OrgD
from fastapi_orgs.types import DependencyCallable


class BaseOrgDatabase(Generic[OrgD]):
    """
    Base adapter for retrieving, creating and updating organizations from a database.

    :param org_db_model: Pydantic model of a DB representation of a organization.
    """

    org_db_model: Type[OrgD]

    def __init__(self, org_db_model: Type[OrgD]):
        self.org_db_model = org_db_model

    async def list(self) -> Optional[OrgD]:
        """Get a list of all organization"""
        raise NotImplementedError()

    async def get(self, id: UUID4) -> Optional[OrgD]:
        """Get a single organization by id."""
        raise NotImplementedError()

    async def create(self, org: OrgD) -> OrgD:
        """Create a organization."""
        raise NotImplementedError()

    async def update(self, org: OrgD) -> OrgD:
        """Update a organization."""
        raise NotImplementedError()

    async def delete(self, org: OrgD) -> None:
        """Delete a organization."""
        raise NotImplementedError()


UserDatabaseDependency = DependencyCallable[BaseOrgDatabase[OrgD]]
