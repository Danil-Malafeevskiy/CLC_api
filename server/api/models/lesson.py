from datetime import datetime, time
from typing import Optional

from pydantic import BaseModel


class LessonResponse(BaseModel):
    id: int
    name: str
    date_lesson: datetime
    duration: float
    price: float
    age: int
    staff_id: int
    staff_position: Optional[str]