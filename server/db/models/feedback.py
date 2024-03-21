from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Integer,
    ForeignKey
)

from .. import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(SmallInteger, primary_key=True)
    text = Column(String, nullable=False)
    parent_id = Column(
        "parent_id", Integer, ForeignKey("parent.id"), nullable=False
    )
    lesson_id = Column(
        "lesson_id", Integer, ForeignKey("lesson.id"), nullable=False
    )