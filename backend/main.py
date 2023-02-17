import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine


def include_router(app):
    app.include_router(api_router)


def configure_static(app):
    script_dir = os.path.dirname(__file__)
    st_abs_file_path = os.path.join(script_dir, "static/")
    app.mount("/static", StaticFiles(directory=st_abs_file_path), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()
