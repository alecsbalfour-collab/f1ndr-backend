from fastapi import FastAPI
from api.routes.search import router as search_router
from api.routes.listings import router as listings_router
from api.routes.scrapers import router as scrapers_router
from api.routes.platforms import router as platforms_router
from api.routes.f1ndr import router as f1ndr_router

app = FastAPI(title="F1NDR Backend")

app.include_router(search_router)
app.include_router(listings_router)
app.include_router(scrapers_router)
app.include_router(platforms_router)
app.include_router(f1ndr_router)
