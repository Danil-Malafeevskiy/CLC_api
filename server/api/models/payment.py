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
    record_id: int = Field(alias="recordId")
    parent_name: Optional[str] = Field(None, alias="parentName")
    lesson_date: Optional[datetime] = Field(None, alias="lessonDate")


class PaymentCreateRequest(BaseModel):
    method: str
    amount: float
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")
    record_id: int = Field(alias="recordId")


class PaymentUpdateRequest(BaseModel):
    method: Optional[str] = None
    amount: Optional[float] = None
    parent_id: Optional[int] = Field(None, alias="parentId")
    lesson_id: Optional[int] = Field(None, alias="lessonId")
    record_id: Optional[int] = Field(None, alias="recordId")


class PaymentListFilter(BaseModel):
    parent_ids: Optional[List[int]] = Field(None, alias="parentIds")
    lesson_ids: Optional[List[int]] = Field(None, alias="lessonIds")
    record_ids: Optional[List[int]] = Field(None, alias="recordIds")
    method: Optional[str] = None

    def apply_to_query(self, query):
        if self.parent_ids:
            query = query.where(Payment.parent_id.in_(self.parent_ids))

        if self.lesson_ids:
            query = query.where(Payment.lesson_id.in_(self.lesson_ids))

        if self.record_ids:
            query = query.where(Payment.record_id.in_(self.record_ids))

        if self.method:
            query = query.where(Payment.method == self.method)

        return query
