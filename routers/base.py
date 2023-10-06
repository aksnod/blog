from fastapi import APIRouter

from routers.v1 import route_blog
from routers.v1 import route_user


api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(route_blog.router, prefix="", tags=["blogs"])