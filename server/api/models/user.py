from typing import Optional, List, Literal

from pydantic import BaseModel, Field

from server.db.models.user import User


class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    email: str
    phone_number: str = Field(alias="phoneNumber")
    address: str
    is_superuser: bool

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserCreateRequest(BaseModel):
    name: str
    username: str
    password: str
    email: str
    phone_number: str = Field(alias="phoneNumber")
    address: str
    is_superuser: Optional[bool] = False

class UserUpdateRequest(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    address: Optional[str] = None


class UserListFilter(BaseModel):
    user_type: List[Literal["*", "parent", "superuser"]] = Field(["*"], alias="userType")

    def apply_to_query(self, query):
        if "*" in self.user_type:
            return query

        if "parent" in self.user_type:
            query = query.where(User.is_superuser == False)

        if "superuser" in self.user_type:
            query = query.where(User.is_superuser == True)

        return query