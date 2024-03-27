import logging
from typing import List, Optional, Tuple

from sqlalchemy import select, delete, text, func
from sqlalchemy.ext.asyncio import AsyncSession

from ..base_models import BaseListNavigation
from ..models.feedback import FeedbackResponse, FeedbackListFilter
from ...api.context import Context
from ...db.models.child import Child
from ...db.models.feedback import Feedback
from ...db.models.lesson import Lesson
from ...db.models.user import User

logger = logging.getLogger("uvicorn")


class FeedbackService:
    @classmethod
    async def create_feedback(cls,
                              text: str,
                              raiting: float,
                              parent_id: int,
                              lesson_id: int,
                              context: Context) -> FeedbackResponse:
        obj = Feedback(
            parent_id=parent_id,
            rating=raiting,
            text=text,
            lesson_id=lesson_id
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return FeedbackResponse(
            id=obj.id,
            raiting=raiting,
            parentId=parent_id,
            text=text,
            lessonId=lesson_id
        )

    @classmethod
    async def get_feedback(cls,
                           id_: int,
                           context: Context) -> FeedbackResponse:
        query = ((select(Feedback, User.name, Lesson.date_lesson).where(Feedback.id == id_)
                 .join(User, User.id == Feedback.parent_id))
                 .join(Lesson, Lesson.id == Feedback.lesson_id)
                 )
        obj, parent_name, lesson_date = (await context.session.execute(query)).first()

        return FeedbackResponse(
            id=obj.id,
            text=obj.text,
            raiting=obj.rating,
            parentId=obj.parent_id,
            lessonId=obj.lesson_id,
            lessonDate=lesson_date,
            parentName=parent_name
        )

    @classmethod
    async def list_feedback(cls,
                            filter_: FeedbackListFilter,
                            navigation: BaseListNavigation,
                            session: AsyncSession) -> Tuple[List[FeedbackResponse], int]:
        query = ((select(Feedback, User.name, Lesson.date_lesson)
                  .join(User, User.id == Feedback.parent_id))
                 .join(Lesson, Lesson.id == Feedback.lesson_id)
                 )

        query = filter_.apply_to_query(query)

        total_q = (
            select(func.count())
            .select_from(query.subquery())
        )

        query = navigation.apply_to_query(query)

        objects = (await session.execute(query))
        count = (await session.execute(total_q)).scalars().first()

        await session.commit()
        await session.close()

        return [
            FeedbackResponse(
                id=obj.id,
                text=obj.text,
                raiting=obj.rating,
                parentId=obj.parent_id,
                lessonId=obj.lesson_id,
                lessonDate=lesson_date,
                parentName=parent_name
            ) for obj, parent_name, lesson_date in objects
        ], count

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
                              raiting: Optional[float],
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

        if raiting:
            obj.rating = raiting
