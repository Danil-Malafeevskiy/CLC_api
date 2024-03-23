from datetime import datetime, time
from typing import Optional, List

from pydantic import BaseModel, Field

from server.db.models.lesson import Lesson


class LessonResponse(BaseModel):
    id: int
    name: str
    date_lesson: datetime
    duration: float
    price: float
    age: int
    staff_id: int
    staff_position: Optional[str] = None


class LessonListFilter(BaseModel):
    staff_ids: Optional[List[int]] = Field(None, alias="staffIds")
    price: Optional[int] = None
    age: Optional[int] = None

    def apply_to_query(self, query):
        if self.staff_ids:
            query = query.where(Lesson.staff_id.in_(self.staff_ids))

        if self.age:
            query = query.where(Lesson.age == self.age)

        if self.price:
            query = query.where(Lesson.price == self.price)

        return query