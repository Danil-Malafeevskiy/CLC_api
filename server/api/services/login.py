import logging

from fastapi import HTTPException
from sqlalchemy import select

from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from ...db.models.user import User

logger = logging.getLogger("uvicorn")


class UserAuthService:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    async def authenticate_user(cls, username: str, password: str, session: AsyncSession):
        user = await cls.get_user_from_username(username, session)

        if not cls.verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        await session.close()

        return user

    @classmethod
    async def get_user_from_username(cls,
                                     username: str,
                                     session: AsyncSession) -> User:
        query = select(User).where(User.username == username)
        obj = (await session.execute(query)).scalars().first()

        if obj is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return obj

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls.pwd_context.verify(plain_password, hashed_password)