from fastapi import APIRouter
from fastapi import Depends

from routers.v1 import route_blog
from routers.v1 import route_login
from routers.v1 import route_user
from routers.v1.route_login import get_current_user


api_router = APIRouter()
api_router.include_router(route_login.router, prefix="", tags=["login"])
api_router.include_router(route_user.router, prefix="/user", tags=["users"])
api_router.include_router(
    route_blog.router,
    prefix="/blog",
    tags=["blogs"],
    dependencies=[Depends(get_current_user)],
)
