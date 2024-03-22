import logging
from typing import List, Optional

from sqlalchemy import select, delete

from ..base_models import BaseListNavigation
from ..models.record import RecordResponse, RecordListFilter
from ...api.context import Context
from ...db.models.child import Child
from ...db.models.lesson import Lesson
from ...db.models.record import Record
from ...db.models.user import User

logger = logging.getLogger("uvicorn")


class RecordService:
    @classmethod
    async def create_record(cls,
                            parent_id: int,
                            child_id: int,
                            lesson_id: int,
                            context: Context) -> RecordResponse:
        obj = Record(
            parent_id=parent_id,
            child_id=child_id,
            lesson_id=lesson_id
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return RecordResponse(
            id=obj.id,
            parentId=parent_id,
            childId=child_id,
            lessonId=lesson_id
        )

    @classmethod
    async def get_record(cls,
                         id_: int,
                         context: Context) -> RecordResponse:
        query = ((select(Record, User.name, Lesson.date_lesson, Child.name).where(Record.id == id_)
                 .join(User, User.id == Record.parent_id))
                 .join(Child, Child.id == Record.child_id)
                 .join(Lesson, Lesson.id == Record.lesson_id)
        )
        obj, parent_name, lesson_date, child_name = (await context.session.execute(query)).first()

        return RecordResponse(
            id=obj.id,
            parentId=obj.parent_id,
            childId=obj.child_id,
            lessonId=obj.lesson_id,
            lessonDate=lesson_date,
            childName=child_name,
            parentName=parent_name
        )

    @classmethod
    async def list_record(cls,
                          filter_: RecordListFilter,
                          navigation: BaseListNavigation,
                          context: Context) -> List[RecordResponse]:
        query = ((select(Record, User.name, Lesson.date_lesson, Lesson.name, Child.name)
                 .join(User, User.id == Record.parent_id))
                 .join(Child, Child.id == Record.child_id)
                 .join(Lesson, Lesson.id == Record.lesson_id)
        )

        query = filter_.apply_to_query(query)
        query = navigation.apply_to_query(query)


        objects = (await context.session.execute(query))

        return [
            RecordResponse(
                id=obj.id,
                parentId=obj.parent_id,
                childId=obj.child_id,
                lessonId=obj.lesson_id,
                lessonDate=lesson_date,
                lessonName=lesson_name,
                childName=child_name,
                parentName=parent_name
            ) for obj, parent_name, lesson_date, lesson_name, child_name in objects
        ]

    @classmethod
    async def remove_record(cls,
                            id_: int,
                            context: Context):
        query = delete(Record).where(Record.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_record(cls,
                            id_: int,
                            parent_id: Optional[int],
                            child_id: Optional[int],
                            lesson_id: Optional[int],
                            context: Context):
        query = select(Record).where(Record.id == id_)
        obj: Record = (await context.session.execute(query)).scalars().first()

        if parent_id:
            obj.parent_id = parent_id

        if child_id:
            obj.child_id = child_id

        if lesson_id:
            obj.lesson_id = lesson_id
