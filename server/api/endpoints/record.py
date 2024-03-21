import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..base_models import BaseListNavigation
from ..context import Context, get_context
from ..models.record import RecordResponse, RecordCreateRequest, RecordUpdateRequest, RecordListFilter
from ..services.record import RecordService

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/record/create", tags=["Record"], name="Record.create")
async def create_record(
        item: RecordCreateRequest = Body(...),
        context: Context = Depends(get_context)) -> RecordResponse:

    record_response = await RecordService.create_record(
        item.parent_id,
        item.child_id,
        item.lesson_id,
        context
    )

    await context.session.commit()
    context.commit()

    return record_response


@router.post(path="/record/get", tags=["Record"], name="Record.get")
async def get_record(
        id_: int = Body(..., description="Identity Record", alias="id"),
        context: Context = Depends(get_context)) -> RecordResponse:

    record_response = await RecordService.get_record(
        id_,
        context
    )

    return record_response


@router.post(path="/record/list", tags=["Record"], name="Record.list")
async def list_record(
        filter_: RecordListFilter = Body(..., alias="filter"),
        navigation: BaseListNavigation = Body(...),
        context: Context = Depends(get_context)) -> List[RecordResponse]:

    record_response = await RecordService.list_record(
        filter_,
        navigation,
        context
    )

    return record_response


@router.post(path="/record/update", tags=["Record"], name="Record.update")
async def update_record(
        id_: int = Body(..., description="Identity Record", alias="id"),
        item: RecordUpdateRequest = Body(...),
        context: Context = Depends(get_context)) -> Dict:

    await RecordService.update_record(
        id_,
        item.parent_id,
        item.child_id,
        item.lesson_id,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/record/remove", tags=["Record"], name="Record.remove")
async def remove_record(
        id_: int = Body(..., description="Identity Record", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await RecordService.remove_record(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}