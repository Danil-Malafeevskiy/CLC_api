from typing import Optional
from fastapi import Request, Response, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from ..db import async_session

security = HTTPBasic()

class Context:
    session: AsyncSession
    session_finished: bool

    def __init__(self,
                 credentials: Optional[HTTPBasicCredentials],
                 request: Optional[Request],
                 response: Optional[Response]):

        self.request = request
        self.response = response

        self.session = async_session()
        self.is_finished = False

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

    def commit(self):
        self.is_finished = True


async def get_context(credentials: Optional[HTTPBasicCredentials] = Depends(security),
                      request: Request = None,
                      response: Response = None):
    async with Context(credentials, request, response) as context:
        yield context