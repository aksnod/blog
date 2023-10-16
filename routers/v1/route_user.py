from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from sqlalchemy.orm import Session

from .route_login import get_current_user
from core.utils import create_upload_file
from db.models import model_user
from db.repository.repo_user import get_user
from db.repository.repo_user import update_profile
from db.session import get_db
from schemas.profile import Profile
from schemas.user import UserBlog

router = APIRouter()


@router.get("/", response_model=UserBlog)
def get_profile(
    current_user: Annotated[model_user.User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    return get_user(current_user.email, db)


@router.post("/profile", response_model=Profile)
async def update_user_profile(
    *,
    first_name: Annotated[str, Form()],
    last_name: Annotated[str | None, Form()] = None,
    address: Annotated[str | None, Form()] = None,
    file: Annotated[UploadFile, File(...)],
    current_user: Annotated[model_user.User, Depends(get_current_user)],
    db: Session = Depends(get_db),
):
    dest = await create_upload_file(file)
    return update_profile(db, current_user.id, first_name, last_name, address, dest)
