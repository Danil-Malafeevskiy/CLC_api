import logging
from typing import Optional, List

from pydantic import BaseModel, Field

from server.db.models.child import Child

logger = logging.getLogger("uvicorn")

class ChildResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str = Field(alias="phoneNumber")
    address: str
    age: int
    gender: str
    parent_id: int = Field(alias="parentId")
    parent_name: Optional[str] = Field(None, alias="parentName")


class ChildCreateRequest(BaseModel):
    name: str
    email: str
    phone_number: str = Field(alias="phoneNumber")
    address: str
    age: int
    gender: str
    parent_id: int = Field(alias="parentId")

class ChildUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    address: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    parent_id: Optional[int] = Field(None, alias="parentId")


class ChildListFilter(BaseModel):
    parent_ids: Optional[List[int]] = Field(None, alias="parentIds")
    gender: Optional[str]
    age: Optional[int]

    def apply_to_query(self, query):
        if self.parent_ids:
            query = query.where(Child.parent_id.in_(self.parent_ids))

        if self.age:
            query = query.where(Child.age == self.age)

        if self.gender:
            query = query.where(Child.gender == self.gender)

        return query
