from pydantic import BaseModel


class BaseComment(BaseModel):
    id: int
    comment: str


class Comment(BaseComment):
    childs: list["Comment"] | None = None

    class config:
        orm_mode = True
