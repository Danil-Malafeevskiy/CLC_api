from pydantic import BaseModel


class StaffResponse(BaseModel):
    id: int
    position: str
    salary: float