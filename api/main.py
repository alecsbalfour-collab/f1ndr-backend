from fastapi import FastAPI
from api.search_route import router as search_router
from api.listings_route import router as listings_router

app = FastAPI(title="F1ndr API")

app.include_router(search_router, prefix="/search")
app.include_router(listings_router, prefix="/listings")
