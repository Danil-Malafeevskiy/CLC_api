from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..settings import (
    DATABASE_URL,
    ENABLE_SQLALCHEMY_LOGGING
)

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=ENABLE_SQLALCHEMY_LOGGING)
Base = declarative_base()
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)