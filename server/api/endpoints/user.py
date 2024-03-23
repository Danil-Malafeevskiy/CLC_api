import logging
from typing import List, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..base_models import BaseListNavigation
from ..context import Context, get_context
from ..models.user import UserResponse, UserCreateRequest, UserUpdateRequest, UserListFilter
from ..services.user import UserService
from ...db import async_session

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/user/create", tags=["User"], name="User.create")
async def create_user(
        item: UserCreateRequest = Body(...)) -> UserResponse:

    user_response = await UserService.create_user(
        item.name,
        item.username,
        item.password,
        item.email,
        item.phone_number,
        item.address,
        item.is_superuser,
        async_session()
    )

    return user_response


@router.post(path="/user/get", tags=["User"], name="User.get")
async def get_user(
        id_: int = Body(..., description="Identity User", alias="id"),
        context: Context = Depends(get_context)) -> UserResponse:

    user_response = await UserService.get_user(
        id_,
        context
    )

    return user_response


@router.post(path="/user/list", tags=["User"], name="User.list")
async def list_user(
        filter_: UserListFilter = Body(..., alias="filter"),
        navigation: BaseListNavigation = Body(...),
        context: Context = Depends(get_context)) -> List[UserResponse]:

    user_response = await UserService.list_user(
        filter_,
        navigation,
        context
    )

    return user_response


@router.post(path="/user/update", tags=["User"], name="User.update")
async def update_user(
        id_: int = Body(..., description="Identity User", alias="id"),
        item: UserUpdateRequest = Body(...),
        context: Context = Depends(get_context)) -> Dict:

    await UserService.update_user(
        id_,
        item.name,
        item.username,
        item.email,
        item.phone_number,
        item.address,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/user/remove", tags=["User"], name="User.remove")
async def remove_user(
        id_: int = Body(..., description="Identity User", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await UserService.remove_user(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}