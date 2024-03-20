import logging
from typing import List, Optional, Dict

from fastapi import Depends, APIRouter, Body
from starlette.status import HTTP_204_NO_CONTENT

from ..context import Context, get_context
from ..models.lesson import LessonResponse
from ..services.lesson import LessonService

logger = logging.getLogger("uvicorn")

router = APIRouter()


@router.post(path="/lesson/create", tags=["Lesson"], name="Lesson.create")
async def create_lesson(
        name: str = Body(...),
        date_lesson: str = Body("2022-01-18 19:00:00", example="2022-01-18 19:00:00"),
        duration: float = Body(...),
        price: float = Body(...),
        age: int = Body(...),
        staff_id: int = Body(...),
        context: Context = Depends(get_context)) -> LessonResponse:

    lesson_response = await LessonService.create_lesson(
        name,
        date_lesson,
        duration,
        price,
        age,
        staff_id,
        context
    )

    await context.session.commit()
    context.commit()

    return lesson_response


@router.post(path="/lesson/get", tags=["Lesson"], name="Lesson.get")
async def get_lesson(
        id_: int = Body(..., description="Identity Lesson", alias="id"),
        context: Context = Depends(get_context)) -> LessonResponse:

    lesson_response = await LessonService.get_lesson(
        id_,
        context
    )

    return lesson_response


@router.post(path="/lesson/list", tags=["Lesson"], name="Lesson.list")
async def list_lesson(
        context: Context = Depends(get_context)) -> List[LessonResponse]:

    lesson_response = await LessonService.list_lesson(
        context
    )

    return lesson_response


@router.post(path="/lesson/update", tags=["Lesson"], name="Lesson.update")
async def update_lesson(
        id_: int = Body(..., description="Identity Lesson", alias="id"),
        name: Optional[str] = Body(None),
        date_lesson: Optional[str] = Body(None, example="2022-01-18 19:00:00"),
        duration: Optional[float] = Body(None),
        price: Optional[float] = Body(None),
        age: Optional[int] = Body(None),
        staff_id: Optional[int] = Body(None),
        context: Context = Depends(get_context)) -> Dict:

    await LessonService.update_lesson(
        id_,
        name,
        date_lesson,
        duration,
        price,
        age,
        staff_id,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}


@router.post(path="/lesson/remove", tags=["Lesson"], name="Lesson.remove")
async def remove_lesson(
        id_: int = Body(..., description="Identity Lesson", alias="id"),
        context: Context = Depends(get_context)) -> Dict:

    await LessonService.remove_lesson(
        id_,
        context
    )

    await context.session.commit()
    context.commit()

    return {"code": HTTP_204_NO_CONTENT}