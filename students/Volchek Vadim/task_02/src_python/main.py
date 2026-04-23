"""
Main entry point for FastAPI app.
"""
from fastapi import FastAPI
import uvicorn

from infrastructure.config import get_container


def create_app() -> FastAPI:
    app = FastAPI(
        title="Bug Service",
        description="Сервис управления багами",
        version="1.0.0",
    )
    container = get_container()
    container.configure_web_app(app)
    return app


app = create_app()


if __name__ == "__main__":
    print("Запуск Bug Service...")
    print("Swagger: http://localhost:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
