from fastapi import FastAPI
from api.routes.f1ndr import router as f1ndr_router
from api.routes.listings import router as listings_router

app = FastAPI(title="f1ndr Backend", version="1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(f1ndr_router, prefix="/f1ndr", tags=["f1ndr"])
app.include_router(listings_router, prefix="/listing", tags=["listing"])
