from sqlalchemy.orm import Session

from db.models.blog import Blog
from schemas.blog import CreateBlog
from schemas.blog import UpdateBlog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def fetch_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def fetch_all_blog(db: Session):
    blogs = db.query(Blog).all()
    return blogs


def update(id: int, author_id: int, blog: UpdateBlog, db: Session):
    blog_in_db = (
        db.query(Blog).filter(Blog.id == id, Blog.author_id == author_id).first()
    )
    if not blog_in_db:
        return {"error": f"Could not find blog with id {id}"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return {"msg": f"updated blog with id {id}"}


def delete(id: int, author_id: int, db: Session):
    print(author_id)
    blog_in_db = db.query(Blog).filter(Blog.id == id, Blog.author_id == author_id)
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id {id}"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"deleted blog with id {id}"}
