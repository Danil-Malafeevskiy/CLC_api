from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class RecordResponse(BaseModel):
    id: int
    parent_id: int = Field(alias="parentId")
    child_id: int = Field(alias="childId")
    lesson_id: int = Field(alias="lessonId")
    lesson_date: Optional[datetime] = Field(None, alias="lessonDate")
    child_name: Optional[str] = Field(None, alias="childName")
    parent_name: Optional[str] = Field(None, alias="parentName")

class RecordCreateRequest(BaseModel):
    parent_id: int = Field(alias="parentId")
    child_id: int = Field(alias="childId")
    lesson_id: int = Field(alias="lessonId")

class RecordUpdateRequest(BaseModel):
    parent_id: Optional[int] = Field(None, alias="parentId")
    child_id: Optional[int] = Field(None, alias="childId")
    lesson_id: Optional[int] = Field(None, alias="lessonId")