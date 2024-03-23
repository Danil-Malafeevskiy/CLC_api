from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .settings import ORIGINS

from .api.endpoints.staff import router as staff_route
from .api.endpoints.lesson import router as lesson_route
from .api.endpoints.user import router as user_route
from .api.endpoints.child import router as child_route
from .api.endpoints.record import router as record_router
from .api.endpoints.feedback import router as feedback_router
from .api.endpoints.payment import router as payment_router
from .api.endpoints.login import router as login_router


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
app.include_router(user_route)
app.include_router(child_route)
app.include_router(record_router)
app.include_router(feedback_router)
app.include_router(payment_router)
app.include_router(login_router)
