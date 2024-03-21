import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..base_models import BaseListNavigation
from ..context import Context, get_context
from ..models.payment import PaymentResponse, PaymentCreateRequest, PaymentUpdateRequest, PaymentListFilter
from ..services.payment import PaymentService

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/payment/create", tags=["Payment"], name="Payment.create")
async def create_payment(
        item: PaymentCreateRequest = Body(...),
        context: Context = Depends(get_context)) -> PaymentResponse:

    payment_response = await PaymentService.create_payment(
        item.method,
        item.amount,
        item.parent_id,
        item.lesson_id,
        context
    )

    await context.session.commit()
    context.commit()

    return payment_response


@router.post(path="/payment/get", tags=["Payment"], name="Payment.get")
async def get_payment(
        id_: int = Body(..., description="Identity Payment", alias="id"),
        context: Context = Depends(get_context)) -> PaymentResponse:

    payment_response = await PaymentService.get_payment(
        id_,
        context
    )

    return payment_response


@router.post(path="/payment/list", tags=["Payment"], name="Payment.list")
async def list_payment(
        filter_: PaymentListFilter = Body(..., alias="filter"),
        navigation: BaseListNavigation = Body(...),
        context: Context = Depends(get_context)) -> List[PaymentResponse]:

    payment_response = await PaymentService.list_payment(
        filter_,
        navigation,
        context
    )

    return payment_response


@router.post(path="/payment/update", tags=["Payment"], name="Payment.update")
async def update_payment(
        id_: int = Body(..., description="Identity Payment", alias="id"),
        item: PaymentUpdateRequest = Body(...),
        context: Context = Depends(get_context)) -> Dict:

    await PaymentService.update_payment(
        id_,
        item.method,
        item.amount,
        item.parent_id,
        item.lesson_id,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/payment/remove", tags=["Payment"], name="Payment.remove")
async def remove_payment(
        id_: int = Body(..., description="Identity Payment", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await PaymentService.remove_payment(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}