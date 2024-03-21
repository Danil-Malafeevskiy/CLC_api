from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from server.db.models.payment import Payment


class PaymentResponse(BaseModel):
    id: int
    method: str
    amount: float
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")
    parent_name: Optional[str] = Field(None, alias="parentName")
    lesson_date: Optional[datetime] = Field(None, alias="lessonDate")


class PaymentCreateRequest(BaseModel):
    method: str
    amount: float
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")


class PaymentUpdateRequest(BaseModel):
    method: Optional[str]
    amount: Optional[float]
    parent_id: Optional[int] = Field(None, alias="parentId")
    lesson_id: Optional[int] = Field(None, alias="lessonId")


class PaymentListFilter(BaseModel):
    parent_ids: Optional[List[int]] = Field(None, alias="parentIds")
    lesson_ids: Optional[List[int]] = Field(None, alias="lessonIds")
    method: Optional[str]

    def apply_to_query(self, query):
        if self.parent_ids:
            query = query.where(Payment.parent_id.in_(self.parent_ids))

        if self.lesson_ids:
            query = query.where(Payment.lesson_id.in_(self.lesson_ids))

        if self.method:
            query = query.where(Payment.method == self.method)

        return query
