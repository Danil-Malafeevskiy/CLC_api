import logging
from typing import List, Optional

from sqlalchemy import select, delete

from ..base_models import BaseListNavigation
from ..models.payment import PaymentResponse, PaymentListFilter
from ...api.context import Context
from ...db.models.payment import Payment
from ...db.models.lesson import Lesson
from ...db.models.user import User

logger = logging.getLogger("uvicorn")


class PaymentService:
    @classmethod
    async def create_payment(cls,
                             method: str,
                             amount: float,
                             parent_id: int,
                             lesson_id: int,
                             context: Context) -> PaymentResponse:
        obj = Payment(
            parent_id=parent_id,
            method=method,
            amount=amount,
            lesson_id=lesson_id
        )

        context.session.add(instance=obj)
        await context.session.flush([obj])

        return PaymentResponse(
            id=obj.id,
            parentId=parent_id,
            method=method,
            amount=amount,
            lessonId=lesson_id
        )

    @classmethod
    async def get_payment(cls,
                          id_: int,
                          context: Context) -> PaymentResponse:
        query = ((select(Payment, User.name, Lesson.date_lesson).where(Payment.id == id_)
                  .join(User, User.id == Payment.parent_id))
                 .join(Lesson, Lesson.id == Payment.lesson_id)
                 )
        obj, parent_name, lesson_date = (await context.session.execute(query)).first()

        return PaymentResponse(
            id=obj.id,
            method=obj.method,
            amount=obj.amount,
            parentId=obj.parent_id,
            lessonId=obj.lesson_id,
            lessonDate=lesson_date,
            parentName=parent_name
        )

    @classmethod
    async def list_payment(cls,
                           filter_: PaymentListFilter,
                           navigation: BaseListNavigation,
                           context: Context) -> List[PaymentResponse]:
        query = ((select(Payment, User.name, Lesson.date_lesson)
                  .join(User, User.id == Payment.parent_id))
                 .join(Lesson, Lesson.id == Payment.lesson_id)
                 )

        query = filter_.apply_to_query(query)
        query = navigation.apply_to_query(query)

        objects = (await context.session.execute(query))

        return [
            PaymentResponse(
                id=obj.id,
                method=obj.method,
                amount=obj.amount,
                parentId=obj.parent_id,
                lessonId=obj.lesson_id,
                lessonDate=lesson_date,
                parentName=parent_name
            ) for obj, parent_name, lesson_date in objects
        ]

    @classmethod
    async def remove_payment(cls,
                             id_: int,
                             context: Context):
        query = delete(Payment).where(Payment.id == id_)
        (await context.session.execute(query))

    @classmethod
    async def update_payment(cls,
                             id_: int,
                             method: Optional[str],
                             amount: Optional[str],
                             parent_id: Optional[int],
                             lesson_id: Optional[int],
                             context: Context):
        query = select(Payment).where(Payment.id == id_)
        obj: Payment = (await context.session.execute(query)).scalars().first()

        if parent_id:
            obj.parent_id = parent_id

        if method:
            obj.method = method

        if amount:
            obj.amount = amount

        if lesson_id:
            obj.lesson_id = lesson_id
