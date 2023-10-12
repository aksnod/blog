from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base import Base


class Profile(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    url = Column(String, nullable=True)
    address = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", uselist=False)

    created_at = Column(DateTime, default=datetime.now)
