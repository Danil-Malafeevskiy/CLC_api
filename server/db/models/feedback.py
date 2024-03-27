from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Integer,
    ForeignKey, Float
)

from .. import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(SmallInteger, primary_key=True)
    text = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    parent_id = Column(
        "parent_id", Integer, ForeignKey("users.id"), nullable=False
    )
    lesson_id = Column(
        "lesson_id", Integer, ForeignKey("lesson.id"), nullable=False
    )