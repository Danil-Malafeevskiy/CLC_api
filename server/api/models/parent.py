from typing import Optional

from pydantic import BaseModel, Field


class ParentResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str = Field(alias="phoneNumber")
    address: str

class ParentCreateRequest(BaseModel):
    name: str
    email: str
    phone_number: str = Field(alias="phoneNumber")
    address: str

class ParentUpdateRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    address: Optional[str]