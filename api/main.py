from fastapi import FastAPI, Request, Response
from f1ndr_backend.config import apply_cors, setup_logging, get_settings
from middleware import (
    ErrorHandlerMiddleware,
    RequestIDMiddleware,
    RequestTimerMiddleware,
)
from security import apply_secure_headers
from routes import (
    dealer_router,
    list_router,
    search_router,
    sell_router,
    watch_router,
)

def create_app() -> FastAPI:
    """
    Build and configure the FastAPI application.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
    )

    # Logging
    setup_logging()

    # CORS
    apply_cors(app)

    # Middleware
    app.add_middleware(ErrorHandlerMiddleware)
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(RequestTimerMiddleware)

    # Routers
    app.include_router(dealer_router)
    app.include_router(list_router)
    app.include_router(search_router)
    app.include_router(sell_router)
    app.include_router(watch_router)

    # Security headers
    @app.middleware("http")
    async def secure_headers_middleware(request: Request, call_next):
        response: Response = await call_next(request)
        apply_secure_headers(response)
        return response

    return app


app = create_app()
