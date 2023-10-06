from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import CreateBlog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def fetch_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog
