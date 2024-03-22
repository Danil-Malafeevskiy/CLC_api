import logging
from datetime import timedelta
from typing import Dict

from fastapi import APIRouter, HTTPException, Body, Depends
from starlette import status

from ..context import get_context, Context
from ..models.login import TokenResponse
from ..models.user import UserLoginRequest
from ..services.login import UserAuthService
from ..utils import create_access_token
from ...db import async_session
from ...settings import ACCESS_TOKEN_EXPIRE_MINUTES

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/token/get", tags=["Token"], name="Token.get")
async def login_for_access_token(
        form_data: UserLoginRequest
) -> TokenResponse:

    user = await UserAuthService.authenticate_user(form_data.username, form_data.password, async_session())

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return TokenResponse(
        id=user.id,
        token=access_token,
        name=user.name,
        username=user.username,
        email=user.email,
        phoneNumber=user.phone_number,
        address=user.address,
        is_superuser=user.is_superuser)


@router.post(path="/token/check", tags=["Token"], name="Token.check")
async def check_access_token(
        context: Context = Depends(get_context)
) -> Dict:

    await context.session.close()

    return {"code": status.HTTP_200_OK}
