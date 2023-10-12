from datetime import datetime

from pydantic import BaseModel
from pydantic import root_validator


class BaseBlog(BaseModel):
    title: str
    content: str | None = None
    slug: str | None = None


class CreateBlog(BaseBlog):
    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class Blog(BaseBlog):
    id: int
    created_at: str | datetime = datetime.now()
    is_active: bool
    author_id: int

    class Config:
        from_attributes = True


class UpdateBlog(CreateBlog):
    pass
