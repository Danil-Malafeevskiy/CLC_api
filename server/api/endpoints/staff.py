import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..context import Context, get_context
from ..models.staff import StaffResponse
from ..services.staff import StaffService

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/staff/create", tags=["Staff"], name="Staff.create")
async def create_staff(
        position: str = Body(..., alice="position"),
        salary: float = Body(..., alias="salary"),
        context: Context = Depends(get_context)) -> StaffResponse:

    staff_response = await StaffService.create_staff(
        position,
        salary,
        context
    )

    await context.session.commit()
    context.commit()

    return staff_response


@router.post(path="/staff/get", tags=["Staff"], name="Staff.get")
async def get_staff(
        id_: int = Body(..., description="Identity Staff", alias="id"),
        context: Context = Depends(get_context)) -> StaffResponse:

    staff_response = await StaffService.get_staff(
        id_,
        context
    )

    return staff_response


@router.post(path="/staff/list", tags=["Staff"], name="Staff.list")
async def list_staff(
        context: Context = Depends(get_context)) -> List[StaffResponse]:

    staff_response = await StaffService.list_staff(
        context
    )

    return staff_response


@router.post(path="/staff/update", tags=["Staff"], name="Staff.update")
async def update_staff(
        id_: int = Body(..., description="Identity Staff", alias="id"),
        position: Optional[str] = Body(None, alice="position"),
        salary: Optional[float] = Body(None, alias="salary"),
        context: Context = Depends(get_context)) -> Dict:

    await StaffService.update_staff(
        id_,
        position,
        salary,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/staff/remove", tags=["Staff"], name="Staff.remove")
async def remove_staff(
        id_: int = Body(..., description="Identity Staff", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await StaffService.remove_staff(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}