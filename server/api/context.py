import asyncio
import logging

from typing import Optional
from fastapi import Request, Response, Depends, HTTPException
from jose import jwt, ExpiredSignatureError, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from ..db import async_session
from ..settings import SECRET_KEY

security = HTTPBearer()

logger = logging.getLogger("uvicorn")


class Context:
    session: AsyncSession
    session_finished: bool

    def __init__(self,
                 credentials: Optional[HTTPAuthorizationCredentials],
                 request: Optional[Request],
                 response: Optional[Response]):

        self.request = request
        self.response = response
        self._credintials = credentials.credentials

        self.session = async_session()
        self.is_finished = False

        self.check_token_correct()


    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None or not self.is_finished:
            await self.session.rollback()
        else:
            await self.session.commit()

        await self.session.close()

        if exc_type is not None:
            return False
        return True

    def check_token_correct(self):
        try:
            jwt.decode(self._credintials, SECRET_KEY, algorithms="HS256")
        except ExpiredSignatureError:
            raise HTTPException(status_code=404, detail="The validity period of the token has ended!")
        except JWTError:
            raise HTTPException(status_code=500, detail="Incorrect token!")

    def commit(self):
        self.is_finished = True


async def get_context(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
                      request: Request = None,
                      response: Response = None):
    async with Context(credentials, request, response) as context:
        yield context