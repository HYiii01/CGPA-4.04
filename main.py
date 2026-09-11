from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import STATIC_DIR
from app.routers import api, pages


def create_app() -> FastAPI:
    application = FastAPI(title="CGPA 4.04")
    application.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
    application.include_router(api.router)
    application.include_router(pages.router)
    return application


app = create_app()