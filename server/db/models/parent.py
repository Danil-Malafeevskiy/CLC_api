from sqlalchemy import (
    Column,
    SmallInteger,
    String
)

from .. import Base


class Parent(Base):
    __tablename__ = "parent"

    id = Column(SmallInteger, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)