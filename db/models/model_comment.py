from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base import Base


class Comments(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="comments")
    blog_id = Column(Integer, ForeignKey("blog.id"))
    blog = relationship("Blog", back_populates="comments")
    parent_id = Column(Integer, ForeignKey("comments.id"))
    childs = relationship("Comments")
