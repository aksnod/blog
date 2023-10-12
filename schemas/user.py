from pydantic import BaseModel
from pydantic import Field

from .blog import BaseBlog
from .profile import BaseProfile


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str = Field(..., min_length=4)


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool


class UserBlog(User):
    blogs: list[BaseBlog] | None = None
    profile: BaseProfile | None = None

    class Config:
        from_attributes = True
