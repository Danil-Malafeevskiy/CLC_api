import logging
from typing import List, Optional

from sqlalchemy import select, delete

from ..models.staff import StaffResponse
from ...api.context import Context
from ...db.models.staff import Staff

logger = logging.getLogger("uvicorn")


class StaffService:
    @classmethod
    async def create_staff(cls,
                           position: str,
                           salary: float,
                           context: Context) -> StaffResponse:
        obj = Staff(position=position, salary=salary)

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return StaffResponse(
            id=obj.id,
            position=obj.position,
            salary=obj.salary
        )

    @classmethod
    async def get_staff(cls,
                        id_: int,
                        context: Context) -> StaffResponse:
        query = select(Staff).where(Staff.id == id_)
        obj = (await context.session.execute(query)).scalars().first()

        return StaffResponse(
            id=obj.id,
            position=obj.position,
            salary=obj.salary
        )

    @classmethod
    async def list_staff(cls,
                         context: Context) -> List[StaffResponse]:
        query = select(Staff)
        objects = (await context.session.execute(query)).scalars().all()

        return [
                StaffResponse(
                    id=obj.id,
                    position=obj.position,
                    salary=obj.salary
                ) for obj in objects
        ]

    @classmethod
    async def remove_staff(cls,
                           id_: int,
                           context: Context):
        query = delete(Staff).where(Staff.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_staff(cls,
                           id_: int,
                           position: Optional[str],
                           salary: Optional[float],
                           context: Context):
        query = select(Staff).where(Staff.id == id_)
        obj: Staff = (await context.session.execute(query)).scalars().first()

        if position:
            obj.position = position

        if salary:
            obj.salary = salary
