from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from db.base import Base


class BlogTag(Base):
    __tablename__ = "blog_tag"
    blog_id = Column(Integer, ForeignKey("blog.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tag.id"), primary_key=True)
