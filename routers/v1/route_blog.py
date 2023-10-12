from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from .route_login import get_current_user
from db.repository.blog import create_new_blog
from db.repository.blog import delete
from db.repository.blog import fetch_all_blog
from db.repository.blog import fetch_blog
from db.repository.blog import update
from db.session import get_db
from schemas.blog import Blog
from schemas.blog import CreateBlog
from schemas.blog import UpdateBlog
from schemas.user import User


router = APIRouter()


@router.post("/blogs", response_model=Blog, status_code=status.HTTP_201_CREATED)
async def create_blog(
    blog: CreateBlog,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return blog


@router.get("/blogs", response_model=list[Blog])
async def get_all_blog(db: Annotated[Session, Depends(get_db)]):
    return fetch_all_blog(db)


@router.get("/blog/{blog_id}")
async def get_blog(
    blog_id: int,
    db: Session = Depends(get_db),
):
    blog = fetch_blog(blog_id, db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {blog_id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.put("/blog/{blog_id}")
async def update_blog(
    blog_id: int,
    blog: UpdateBlog,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return update(blog_id, current_user.id, blog, db)


@router.delete("/blog/{blog_id}")
async def delete_blog(
    blog_id: int,
    db: Annotated[Session, Depends(get_db)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return delete(blog_id, current_user.id, db)
