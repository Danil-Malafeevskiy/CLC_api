from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .settings import ORIGINS

from .api.endpoints.staff import router as staff_route
from .api.endpoints.lesson import router as lesson_route
from .api.endpoints.parent import router as parent_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(staff_route)
app.include_router(lesson_route)
app.include_router(parent_route)