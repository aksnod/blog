from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.profile import Profile
from db.models.user import User
from schemas.user import UserCreate


def create_new_user(user: UserCreate, db: Session):
    user_in_db = get_user(user.email, db)
    if user_in_db:
        return user
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def update_profile(
    db: Session,
    user_id: int,
    first_name: str,
    last_name: str | None = None,
    address: str | None = None,
    url: str | None = None,
):
    profile_in_db = db.query(Profile).filter(Profile.user_id == user_id).first()
    if profile_in_db:
        profile_in_db.first_name = first_name
        profile_in_db.last_name = last_name
        profile_in_db.address = address
        profile_in_db.url = url
        db.add(profile_in_db)
        db.commit()
        return profile_in_db
    else:
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            address=address,
            url=url,
            user_id=user_id,
        )
        db.add(profile)
        db.commit()
        db.refresh(profile)
        return profile
