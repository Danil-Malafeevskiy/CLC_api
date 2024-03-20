import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..context import Context, get_context
from ..models.parent import ParentResponse, ParentCreateRequest, ParentUpdateRequest
from ..services.parent import ParentService

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/parent/create", tags=["Parent"], name="Parent.create")
async def create_parent(
        item: ParentCreateRequest = Body(...),
        context: Context = Depends(get_context)) -> ParentResponse:

    parent_response = await ParentService.create_parent(
        item.name,
        item.email,
        item.phone_number,
        item.address,
        context
    )

    await context.session.commit()
    context.commit()

    return parent_response


@router.post(path="/parent/get", tags=["Parent"], name="Parent.get")
async def get_parent(
        id_: int = Body(..., description="Identity Parent", alias="id"),
        context: Context = Depends(get_context)) -> ParentResponse:

    parent_response = await ParentService.get_parent(
        id_,
        context
    )

    return parent_response


@router.post(path="/parent/list", tags=["Parent"], name="Parent.list")
async def list_parent(
        context: Context = Depends(get_context)) -> List[ParentResponse]:

    parent_response = await ParentService.list_parent(
        context
    )

    return parent_response


@router.post(path="/parent/update", tags=["Parent"], name="Parent.update")
async def update_parent(
        id_: int = Body(..., description="Identity Parent", alias="id"),
        item: ParentUpdateRequest = Body(...),
        context: Context = Depends(get_context)) -> Dict:

    await ParentService.update_parent(
        id_,
        item.name,
        item.email,
        item.phone_number,
        item.address,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/parent/remove", tags=["Parent"], name="Parent.remove")
async def remove_parent(
        id_: int = Body(..., description="Identity Parent", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await ParentService.remove_parent(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}