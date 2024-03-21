from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

from server.db.models.record import Record


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


class RecordListFilter(BaseModel):
    parent_ids: Optional[List[int]] = Field(None, alias="parentIds")
    child_ids: Optional[List[int]] = Field(None, alias="childIds")
    lesson_ids: Optional[List[int]] = Field(None, alias="lessonIds")

    def apply_to_query(self, query):
        if self.parent_ids:
            query = query.where(Record.parent_id.in_(self.parent_ids))

        if self.lesson_ids:
            query = query.where(Record.lesson_id.in_(self.lesson_ids))

        if self.child_ids:
            query = query.where(Record.child_id.in_(self.child_ids))

        return query
