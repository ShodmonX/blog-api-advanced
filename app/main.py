from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.core.exceptions import AppError
from app.api.router import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Blog API",
        description="A simple blog API built with FastAPI and SQLAlchemy",
        version="1.0.0",
    )

    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                    "details": exc.details,
                }
            },
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "error": {
                    "code": "validation_error",
                    "message": "Validation failed",
                    "details": exc.errors(),
                }
            },
        )
    
    app.include_router(router)

    return app

app = create_app()