from sqlalchemy import (
    Column,
    SmallInteger,
    String, Boolean, UniqueConstraint
)

from .. import Base


class User(Base):
    __tablename__ = "users"

    id = Column(SmallInteger, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    UniqueConstraint("username", name="uix_1")
