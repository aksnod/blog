from datetime import datetime

from pydantic import BaseModel


class BaseProfile(BaseModel):
    first_name: str
    last_name: str | None = None
    address: str | None = None
    url: str | None = None


class CreateProfile(BaseProfile):
    pass


class Profile(BaseProfile):
    id: int
    user_id: int
    created_at: str | datetime = datetime.now()


class UpdateProfile(CreateProfile):
    pass
