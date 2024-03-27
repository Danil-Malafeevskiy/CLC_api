import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..base_models import BaseListNavigation
from ..context import Context, get_context
from ..models.feedback import FeedbackResponse, FeedbackCreateRequest, FeedbackUpdateRequest, FeedbackListFilter
from ..services.feedback import FeedbackService
from ...db import async_session

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/feedback/create", tags=["Feedback"], name="Feedback.create")
async def create_feedback(
        item: FeedbackCreateRequest = Body(...),
        context: Context = Depends(get_context)) -> FeedbackResponse:

    feedback_response = await FeedbackService.create_feedback(
        item.text,
        item.parent_id,
        item.lesson_id,
        context
    )

    await context.session.commit()
    context.commit()

    return feedback_response


@router.post(path="/feedback/get", tags=["Feedback"], name="Feedback.get")
async def get_feedback(
        id_: int = Body(..., description="Identity Feedback", alias="id"),
        context: Context = Depends(get_context)) -> FeedbackResponse:

    feedback_response = await FeedbackService.get_feedback(
        id_,
        context
    )

    return feedback_response


@router.post(path="/feedback/list", tags=["Feedback"], name="Feedback.list")
async def list_feedback(
        filter_: FeedbackListFilter = Body(..., alias="filter"),
        navigation: BaseListNavigation = Body(...)) -> List[FeedbackResponse]:

    feedback_response = await FeedbackService.list_feedback(
        filter_,
        navigation,
        async_session()
    )

    return feedback_response


@router.post(path="/feedback/update", tags=["Feedback"], name="Feedback.update")
async def update_feedback(
        id_: int = Body(..., description="Identity Feedback", alias="id"),
        item: FeedbackUpdateRequest = Body(...),
        context: Context = Depends(get_context)) -> Dict:

    await FeedbackService.update_feedback(
        id_,
        item.text,
        item.parent_id,
        item.lesson_id,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/feedback/remove", tags=["Feedback"], name="Feedback.remove")
async def remove_feedback(
        id_: int = Body(..., description="Identity Feedback", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await FeedbackService.remove_feedback(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}