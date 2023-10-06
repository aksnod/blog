from pydantic import BaseModel
from pydantic import Field


class UserCreate(BaseModel):
    email: str
    password: str = Field(..., min_length=8)
