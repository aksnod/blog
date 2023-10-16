from fastapi import FastAPI

from core.config import settings
from db import Base
from db.session import engine
from routers.base import api_router


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    ENVIRONMENT = settings.env  # get current env name
    print(ENVIRONMENT)
    SHOW_DOCS_ENVIRONMENT = ("local", "dev")  # explicit list of allowed envs

    app_configs = {"title": settings.PROJECT_NAME, "version": settings.PROJECT_VERSION}
    if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
        app_configs["openapi_url"] = None
    app = FastAPI(**app_configs)
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
