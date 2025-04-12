from fastapi import FastAPI
from app.api import registration
from app.containers import Container
from app.core.config import settings
from app.core.middleware import LoggerContextMiddleware, AuthMiddleware
from app.core.logging import setup_logging

def create_app() -> FastAPI:
    container = Container()
    container.config.from_pydantic(settings)

    app = FastAPI()
    app.container = container

    # Setup logging
    logger = setup_logging()
    app.logger = logger

    # Add middlewares
    app.add_middleware(LoggerContextMiddleware)
    app.add_middleware(AuthMiddleware)

    app.include_router(registration.router)

    return app
 
app = create_app()
