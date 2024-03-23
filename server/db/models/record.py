from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Integer,
    ForeignKey
)

from .. import Base


class Record(Base):
    __tablename__ = "record"

    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(
        "parent_id", Integer, ForeignKey("users.id"), nullable=False
    )
    child_id = Column(
        "child_id", Integer, ForeignKey("child.id"), nullable=False
    )
    lesson_id = Column(
        "lesson_id", Integer, ForeignKey("lesson.id"), nullable=False
    )