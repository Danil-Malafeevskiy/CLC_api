from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


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