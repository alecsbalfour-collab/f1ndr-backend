from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your active controller routers
from api.controllers.search_controller import router as search_router
from api.controllers.dealer_controller import router as dealer_router
from api.controllers.sell_controller import router as sell_router

app = FastAPI(
    title="f1ndr API Engine",
    description="Enterprise endpoints for FlutterFlow schema integration",
    version="1.0.0"
)

# Enable CORS middleware (Crucial: stops FlutterFlow from blocking your client calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Explicitly register the routers onto the main orchestration app instance
app.include_router(search_router)
app.include_router(dealer_router)
app.include_router(sell_router)

@app.get("/")
async def root():
    return {"status": "operational", "message": "f1ndr API Engine is fully linked"}
