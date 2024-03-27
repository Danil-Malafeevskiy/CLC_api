from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from server.db.models.feedback import Feedback


class FeedbackResponse(BaseModel):
    id: int
    text: str
    raiting: float
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")
    parent_name: Optional[str] = Field(None, alias="parentName")
    lesson_date: Optional[datetime] = Field(None, alias="lessonDate")

class FeedbackCreateRequest(BaseModel):
    text: str
    raiting: float
    parent_id: int = Field(alias="parentId")
    lesson_id: int = Field(alias="lessonId")

class FeedbackUpdateRequest(BaseModel):
    text: Optional[str]
    raiting: Optional[float]
    parent_id: Optional[int] = Field(None, alias="parentId")
    lesson_id: Optional[int] = Field(None, alias="lessonId")


class FeedbackListFilter(BaseModel):
    raiting: Optional[float] = Field(None)
    parent_ids: Optional[List[int]] = Field(None, alias="parentIds")
    lesson_ids: Optional[List[int]] = Field(None, alias="lessonIds")

    def apply_to_query(self, query):
        if self.raiting:
            query = query.where(Feedback.raiting == self.raiting)

        if self.parent_ids:
            query = query.where(Feedback.parent_id.in_(self.parent_ids))

        if self.lesson_ids:
            query = query.where(Feedback.lesson_id.in_(self.lesson_ids))

        return query
