import logging
from typing import List, Optional

from sqlalchemy import select, delete

from ..models.Child import ChildResponse
from ...api.context import Context
from ...db.models.child import Child
from ...db.models.parent import Parent

logger = logging.getLogger("uvicorn")


class ChildService:
    @classmethod
    async def create_child(cls,
                           name: str,
                           email: str,
                           phone_number: str,
                           address: str,
                           age: int,
                           gender: str,
                           parent_id: int,
                           context: Context) -> ChildResponse:
        obj = Child(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            age=age,
            gender=gender,
            parent_id=parent_id
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return ChildResponse(
            id=obj.id,
            name=name,
            email=email,
            phoneNumber=phone_number,
            address=address,
            age=age,
            gender=gender,
            parentId=parent_id
        )

    @classmethod
    async def get_child(cls,
                        id_: int,
                        context: Context) -> ChildResponse:
        query = select(Child, Parent.name).where(Child.id == id_).join(Parent, Parent.id == Child.parent_id)
        obj, parent = (await context.session.execute(query)).first()

        return ChildResponse(
            id=obj.id,
            name=obj.name,
            email=obj.email,
            phoneNumber=obj.phone_number,
            address=obj.address,
            age=obj.age,
            gender=obj.gender,
            parentId=obj.parent_id,
            parentName=parent.name
        )

    @classmethod
    async def list_child(cls,
                         context: Context) -> List[ChildResponse]:
        query = select(Child, Parent.name)
        objects = (await context.session.execute(query))

        return [
            ChildResponse(
                id=obj.id,
                name=obj.name,
                email=obj.email,
                phoneNumber=obj.phone_number,
                address=obj.address,
                age=obj.age,
                gender=obj.gender,
                parentId=obj.parent_id,
                parentName=parent_name
            ) for obj, parent_name in objects
        ]

    @classmethod
    async def remove_child(cls,
                           id_: int,
                           context: Context):
        query = delete(Child).where(Child.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_child(cls,
                           id_: int,
                           name: Optional[str],
                           email: Optional[str],
                           phone_number: Optional[str],
                           address: Optional[str],
                           age: Optional[int],
                           gender: Optional[str],
                           parent_id: Optional[int],
                           context: Context):
        query = select(Child).where(Child.id == id_)
        obj: Child = (await context.session.execute(query)).scalars().first()

        if name:
            obj.name = name

        if email:
            obj.email = email

        if phone_number:
            obj.phone_number = phone_number

        if address:
            obj.address = address

        if age:
            obj.age = age

        if gender:
            obj.gender = gender

        if parent_id:
            obj.parent_id = parent_id
