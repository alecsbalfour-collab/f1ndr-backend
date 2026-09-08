# f1ndr_backend/api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Settings
from api.config.settings_config import get_settings

# DB
from db.connection_db import connect_to_db
from db.indexing_db import apply_indexes
from db.ttl_db import apply_ttl

# Security
from api.security.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from api.middleware.abuse_middleware import AbuseMiddleware
from api.security.api_key_validator import APIKeyValidator

# Logging
import logging
from logs.structured_logger import StructuredLogger

# Scheduler
from scheduler.cleanup_jobs import (
    cleanup_ingestion_temp,
    cleanup_old_logs,
)

# Routers
from api.controllers.search_controller import router as search_router
from api.controllers.dealer_controller import router as dealer_router
from api.controllers.sell_controller import router as sell_router


# ---------------------------------------------------------
# App Initialization
# ---------------------------------------------------------

settings = get_settings()
app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# Render-friendly logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
startup_logger = StructuredLogger("startup")


# ---------------------------------------------------------
# Middleware
# ---------------------------------------------------------

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate Limiting
app.state.limiter = limiter