from typing import Optional

from pydantic import BaseModel, Field


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