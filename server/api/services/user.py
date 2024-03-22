import logging
from typing import List, Optional

from sqlalchemy import select, delete

from passlib.context import CryptContext

from ..base_models import BaseListNavigation
from ..models.user import UserResponse, UserListFilter
from ...api.context import Context
from ...db.models.user import User

logger = logging.getLogger("uvicorn")


class UserService:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    async def create_user(cls,
                          name: str,
                          username: str,
                          password: str,
                          email: str,
                          phone_number: str,
                          address: str,
                          is_superuser: bool,
                          context: Context) -> UserResponse:
        obj = User(
            name=name,
            username=username,
            password=cls.get_password_hash(password),
            email=email,
            phone_number=phone_number,
            address=address,
            is_superuser=is_superuser
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return UserResponse(
            id=obj.id,
            name=name,
            username=username,
            email=email,
            phoneNumber=phone_number,
            address=address,
            is_superuser=is_superuser
        )

    @classmethod
    async def get_user(cls,
                       id_: int,
                       context: Context) -> UserResponse:
        query = select(User).where(User.id == id_)
        obj = (await context.session.execute(query)).scalars().first()

        return UserResponse(
            id=obj.id,
            name=obj.name,
            username=obj.username,
            email=obj.email,
            phoneNumber=obj.phone_number,
            address=obj.address,
            is_superuser=obj.is_superuser
        )

    @classmethod
    async def list_user(cls,
                        filter_: UserListFilter,
                        navigation: BaseListNavigation,
                        context: Context) -> List[UserResponse]:
        query = select(User)

        query = filter_.apply_to_query(query)
        query = navigation.apply_to_query(query)

        objects = (await context.session.execute(query)).scalars().all()

        return [
            UserResponse(
                id=obj.id,
                name=obj.name,
                username=obj.username,
                email=obj.email,
                phoneNumber=obj.phone_number,
                address=obj.address,
                is_superuser=obj.is_superuser
            ) for obj in objects
        ]

    @classmethod
    async def remove_user(cls,
                          id_: int,
                          context: Context):
        query = delete(User).where(User.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_user(cls,
                          id_: int,
                          name: Optional[str],
                          username: Optional[str],
                          email: Optional[str],
                          phone_number: Optional[str],
                          address: Optional[str],
                          context: Context):
        query = select(User).where(User.id == id_)
        obj: User = (await context.session.execute(query)).scalars().first()

        if name:
            obj.name = name

        if email:
            obj.email = email

        if phone_number:
            obj.phone_number = phone_number

        if address:
            obj.address = address

        if username:
            obj.username = username

    @classmethod
    def get_password_hash(cls, password):
        return cls.pwd_context.hash(password)
