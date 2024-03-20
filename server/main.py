from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .settings import ORIGINS

from .api.endpoints.staff import router as staff_route
from .api.endpoints.lesson import router as lesson_route
from .api.endpoints.parent import router as parent_route
from .api.endpoints.Child import router as child_route
#from .api.endpoints.record import router as record_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(staff_route)
app.include_router(lesson_route)
app.include_router(parent_route)
app.include_router(child_route)
#app.include_router(record_router)