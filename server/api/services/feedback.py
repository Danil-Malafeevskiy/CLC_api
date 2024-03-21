import logging
from typing import List, Optional

from sqlalchemy import select, delete

from ..models.feedback import FeedbackResponse
from ...api.context import Context
from ...db.models.child import Child
from ...db.models.feedback import Feedback
from ...db.models.lesson import Lesson
from ...db.models.parent import Parent

logger = logging.getLogger("uvicorn")


class FeedbackService:
    @classmethod
    async def create_feedback(cls,
                              text: str,
                              parent_id: int,
                              lesson_id: int,
                              context: Context) -> FeedbackResponse:
        obj = Feedback(
            parent_id=parent_id,
            text=text,
            lesson_id=lesson_id
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return FeedbackResponse(
            id=obj.id,
            parentId=parent_id,
            text=text,
            lessonId=lesson_id
        )

    @classmethod
    async def get_feedback(cls,
                           id_: int,
                           context: Context) -> FeedbackResponse:
        query = ((select(Feedback, Parent.name, Lesson.date_lesson).where(Feedback.id == id_)
                 .join(Parent, Parent.id == Feedback.parent_id))
                 .join(Lesson, Lesson.id == Feedback.lesson_id)
                 )
        obj, parent_name, lesson_date = (await context.session.execute(query)).first()

        return FeedbackResponse(
            id=obj.id,
            text=obj.text,
            parentId=obj.parent_id,
            lessonId=obj.lesson_id,
            lessonDate=lesson_date,
            parentName=parent_name
        )

    @classmethod
    async def list_feedback(cls,
                            context: Context) -> List[FeedbackResponse]:
        query = ((select(Feedback, Parent.name, Lesson.date_lesson)
                  .join(Parent, Parent.id == Feedback.parent_id))
                 .join(Lesson, Lesson.id == Feedback.lesson_id)
                 )
        objects = (await context.session.execute(query))

        return [
            FeedbackResponse(
                id=obj.id,
                text=obj.text,
                parentId=obj.parent_id,
                lessonId=obj.lesson_id,
                lessonDate=lesson_date,
                parentName=parent_name
            ) for obj, parent_name, lesson_date in objects
        ]

    @classmethod
    async def remove_feedback(cls,
                              id_: int,
                              context: Context):
        query = delete(Feedback).where(Feedback.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_feedback(cls,
                              id_: int,
                              text: Optional[str],
                              parent_id: Optional[int],
                              lesson_id: Optional[int],
                              context: Context):
        query = select(Feedback).where(Feedback.id == id_)
        obj: Feedback = (await context.session.execute(query)).scalars().first()

        if parent_id:
            obj.parent_id = parent_id

        if text:
            obj.text = text

        if lesson_id:
            obj.lesson_id = lesson_id
