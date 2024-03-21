from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FeedbackResponse(BaseModel):
    id: int
    text: str
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")
    parent_name: Optional[str] = Field(None, alias="parentName")
    lesson_date: Optional[datetime] = Field(None, alias="lessonDate")

class FeedbackCreateRequest(BaseModel):
    text: str
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")

class FeedbackUpdateRequest(BaseModel):
    text: Optional[str]
    parent_id: Optional[int] = Field(None, alias="parentId")
    lesson_id: Optional[int] = Field(None, alias="lessonId")