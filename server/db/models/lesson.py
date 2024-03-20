from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Float,
    Integer,
    Time, ForeignKey,
    TIMESTAMP, DATETIME
)

from .. import Base


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(SmallInteger, primary_key=True)
    name = Column(String, nullable=False)
    date_lesson = Column(DATETIME, nullable=False)
    duration = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    age = Column(SmallInteger, nullable=False)
    staff_id = Column(
        "staff_id", Integer, ForeignKey("staff.id"), nullable=False
    )
