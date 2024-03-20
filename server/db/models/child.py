from sqlalchemy import (
    Column,
    SmallInteger,
    String,
    Integer,
    ForeignKey
)

from .. import Base


class Child(Base):
    __tablename__ = "child"

    id = Column(SmallInteger, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    age = Column(SmallInteger, nullable=False)
    gender = Column(String, nullable=False)
    parent_id = Column(
        "parent_id", Integer, ForeignKey("parent.id"), nullable=False
    )