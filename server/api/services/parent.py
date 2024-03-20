import logging
from typing import List, Optional

from sqlalchemy import select, delete

from ..models.parent import ParentResponse
from ...api.context import Context
from ...db.models.parent import Parent

logger = logging.getLogger("uvicorn")


class ParentService:
    @classmethod
    async def create_parent(cls,
                            name: str,
                            email: str,
                            phone_number: str,
                            address: str,
                            context: Context) -> ParentResponse:
        obj = Parent(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return ParentResponse(
            id=obj.id,
            name=obj.name,
            email=obj.email,
            phoneNumber=obj.phone_number,
            address=obj.address
        )

    @classmethod
    async def get_parent(cls,
                         id_: int,
                         context: Context) -> ParentResponse:
        query = select(Parent).where(Parent.id == id_)
        obj = (await context.session.execute(query)).scalars().first()

        return ParentResponse(
            id=obj.id,
            name=obj.name,
            email=obj.email,
            phoneNumber=obj.phone_number,
            address=obj.address
        )

    @classmethod
    async def list_parent(cls,
                          context: Context) -> List[ParentResponse]:
        query = select(Parent)
        objects = (await context.session.execute(query)).scalars().all()

        return [
            ParentResponse(
                id=obj.id,
                name=obj.name,
                email=obj.email,
                phoneNumber=obj.phone_number,
                address=obj.address
            ) for obj in objects
        ]

    @classmethod
    async def remove_parent(cls,
                            id_: int,
                            context: Context):
        query = delete(Parent).where(Parent.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_parent(cls,
                            id_: int,
                            name: Optional[str],
                            email: Optional[str],
                            phone_number: Optional[str],
                            address: Optional[str],
                            context: Context):
        query = select(Parent).where(Parent.id == id_)
        obj: Parent = (await context.session.execute(query)).scalars().first()

        if name:
            obj.name = name

        if email:
            obj.email = email

        if phone_number:
            obj.phone_number = phone_number

        if address:
            obj.address = address
