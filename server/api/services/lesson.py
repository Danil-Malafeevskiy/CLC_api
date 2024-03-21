import logging
import time
from datetime import datetime
from typing import List, Optional

from sqlalchemy import delete, select
from sqlalchemy.orm import aliased

from ..base_models import BaseListNavigation
from ..models.lesson import LessonResponse, LessonListFilter
from ...api.context import Context
from ...db.models.lesson import Lesson
from ...db.models.staff import Staff

logger = logging.getLogger("uvicorn")


class LessonService:
    @classmethod
    async def create_lesson(cls,
                            name: str,
                            date_lesson: str,
                            duration: float,
                            price: float,
                            age: int,
                            staff_id: int,
                            context: Context) -> LessonResponse:
        obj = Lesson(
            name=name,
            date_lesson=datetime.strptime(date_lesson, "%Y-%m-%d %H:%M:%S"),
            duration=duration,
            price=price,
            age=age,
            staff_id=staff_id
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return LessonResponse(
            id=obj.id,
            name=obj.name,
            date_lesson=obj.date_lesson,
            duration=obj.duration,
            price=obj.price,
            age=obj.age,
            staff_id=obj.staff_id
        )

    @classmethod
    async def get_lesson(cls,
                         id_: int,
                         context: Context) -> LessonResponse:
        query = select(Lesson, Staff.position).where(Lesson.id == id_).join(Staff, Staff.id == Lesson.staff_id)
        obj, pos = (await context.session.execute(query)).first()

        return LessonResponse(
            id=obj.id,
            name=obj.name,
            date_lesson=obj.date_lesson,
            duration=obj.duration,
            price=obj.price,
            age=obj.age,
            staff_id=obj.staff_id,
            staff_position=pos
        )

    @classmethod
    async def list_lesson(cls,
                          filter_: LessonListFilter,
                          navigation: BaseListNavigation,
                          context: Context) -> List[LessonResponse]:
        query = select(Lesson, Staff.position).join(Staff, Staff.id == Lesson.staff_id)

        query = filter_.apply_to_query(query)
        query = navigation.apply_to_query(query)

        objects = (await context.session.execute(query))

        return [
            LessonResponse(
                id=obj.id,
                name=obj.name,
                date_lesson=obj.date_lesson,
                duration=obj.duration,
                price=obj.price,
                age=obj.age,
                staff_id=obj.staff_id,
                staff_position=pos
            ) for obj, pos in objects
        ]

    @classmethod
    async def remove_lesson(cls,
                            id_: int,
                            context: Context):
        query = delete(Lesson).where(Lesson.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_lesson(cls,
                            id_: int,
                            name: Optional[str],
                            date_lesson: str,
                            duration: Optional[float],
                            price: Optional[float],
                            age: Optional[int],
                            staff_id: Optional[int],
                            context: Context):
        query = select(Lesson).where(Lesson.id == id_)
        obj: Lesson = (await context.session.execute(query)).scalars().first()

        if name:
            obj.name = name

        if date_lesson:
            obj.date_lesson = datetime.strptime(date_lesson, "%Y-%m-%d %H:%M:%S")

        if duration:
            obj.duration = duration

        if price:
            obj.price = price

        if age:
            obj.age = age

        if staff_id:
            obj.staff_id = staff_id
