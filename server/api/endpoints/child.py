import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..base_models import BaseListNavigation
from ..context import Context, get_context
from ..models.child import ChildResponse, ChildCreateRequest, ChildUpdateRequest, ChildListFilter
from ..services.child import ChildService

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/child/create", tags=["Child"], name="Child.create")
async def create_child(
        item: ChildCreateRequest = Body(...),
        context: Context = Depends(get_context)) -> ChildResponse:

    child_response = await ChildService.create_child(
        item.name,
        item.email,
        item.phone_number,
        item.address,
        item.age,
        item.gender,
        item.parent_id,
        context
    )

    await context.session.commit()
    context.commit()

    return child_response


@router.post(path="/child/get", tags=["Child"], name="Child.get")
async def get_child(
        id_: int = Body(..., description="Identity Child", alias="id"),
        context: Context = Depends(get_context)) -> ChildResponse:

    child_response = await ChildService.get_child(
        id_,
        context
    )

    return child_response


@router.post(path="/child/list", tags=["Child"], name="Child.list")
async def list_child(
        filter_: ChildListFilter = Body(..., alias="filter"),
        navigation: BaseListNavigation = Body(...),
        context: Context = Depends(get_context)) -> List[ChildResponse]:

    child_response = await ChildService.list_child(
        filter_,
        navigation,
        context
    )

    return child_response


@router.post(path="/child/update", tags=["Child"], name="Child.update")
async def update_child(
        id_: int = Body(..., description="Identity Child", alias="id"),
        item: ChildUpdateRequest = Body(...),
        context: Context = Depends(get_context)) -> Dict:

    await ChildService.update_child(
        id_,
        item.name,
        item.email,
        item.phone_number,
        item.address,
        item.age,
        item.gender,
        item.parent_id,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/child/remove", tags=["Child"], name="Child.remove")
async def remove_child(
        id_: int = Body(..., description="Identity Child", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await ChildService.remove_child(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}