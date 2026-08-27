from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ROUTERS (correct path: api/routes/)
from api.routes.listings import router as listings_router
from api.routes.search import router as search_router
from api.routes.health import router as health_router
from api.routes.platforms import router as platforms_router
from api.routes.filters import router as filters_router
from api.routes.status import router as status_router

app = FastAPI(
    title="F1ndr Backend",
    version="1.0.0",
    description="Enterprise backend powering F1ndr multi-platform search."
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# INCLUDE ALL ROUTERS
app.include_router(listings_router)
app.include_router(search_router)
app.include_router(health_router)
app.include_router(platforms_router)
app.include_router(filters_router)
app.include_router(status_router)
