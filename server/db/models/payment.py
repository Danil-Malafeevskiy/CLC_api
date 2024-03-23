from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Integer,
    ForeignKey, Float
)

from .. import Base


class Payment(Base):
    __tablename__ = "payment"

    id = Column(SmallInteger, primary_key=True)
    method = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    parent_id = Column(
        "parent_id", Integer, ForeignKey("users.id"), nullable=False
    )
    lesson_id = Column(
        "lesson_id", Integer, ForeignKey("lesson.id"), nullable=False
    )