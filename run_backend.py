import uvicorn
from fastapi import FastAPI

from api.config.settings_config import get_settings
from api.config.cors_config import get_cors_middleware
from api.config.logging_config import configure_logging

from api.middleware.error_handler_middleware import add_error_handler_middleware
from api.middleware.request_id_middleware import add_request_id_middleware
from api.middleware.request_timer_middleware import add_request_timer_middleware
from api.security.secure_header import add_secure_headers

from api.routes.search_routes import router as search_router
from api.controllers.health_controller import get_health

from api.logging.api_logger import get_api_logger

from db.connection_db import get_db_client
from scrapers.db.scrapers_db_connection import get_scraper_db_client


def create_app() -> FastAPI:
    settings = get_settings()

    configure_logging(settings)

    app = FastAPI(
        title=settings.api_name,
        version=settings.api_version,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Middleware
    get_cors_middleware(app, settings)
    add_error_handler_middleware(app)
    add_request_id_middleware(app)
    add_request_timer_middleware(app)
    add_secure_headers(app)

    # Routes
    app.include_router(search_router, prefix="/search", tags=["search"])

    @app.get("/health", tags=["health"])
    async def health():
        return get_health(settings.api_version)

    logger = get_api_logger()

    @app.on_event("startup")
    async def startup_event():
        logger.info("startup.begin")
        get_db_client().connect()
        get_scraper_db_client().connect()
        logger.info("startup.complete")

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("shutdown.begin")
        get_db_client().disconnect()
        get_scraper_db_client().disconnect()
        logger.info("shutdown.complete")

    return app


app = create_app()


if __name__ == "__main__":
    settings = get_settings()

    uvicorn.run(
        "run_backend:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True,
        log_level=settings.log_level.lower(),
    )
