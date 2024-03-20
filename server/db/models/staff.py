from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Float
)

from .. import Base


class Staff(Base):
    __tablename__ = "staff"

    id = Column(SmallInteger, primary_key=True)
    position = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
