# app/main.py
from fastapi import FastAPI
from app.containers import ApplicationContainer
from app.routes.v1.root import router as message_router

def create_app() -> FastAPI:
    container = ApplicationContainer()

    container.wire(
        modules=[
            __name__,
            "app.routes.v1.root",
        ]
    )

    app = FastAPI()
    app.container = container

    app.include_router(message_router, prefix="/v1", tags=["Message"])

    return app

app = create_app()