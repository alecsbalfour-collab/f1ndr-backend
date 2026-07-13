from fastapi import FastAPI
from api.routes import listings, platforms, categories, insights, scrapers, discovery

app = FastAPI(title="watcHr API", version="1.0")

# Register routes
app.include_router(listings.router, prefix="/listings", tags=["Listings"])
app.include_router(platforms.router, prefix="/platforms", tags=["Platforms"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(insights.router, prefix="/insights", tags=["Insights"])
app.include_router(scrapers.router, prefix="/scrapers", tags=["Scrapers"])
app.include_router(discovery.router, prefix="/discovery", tags=["Discovery"])
