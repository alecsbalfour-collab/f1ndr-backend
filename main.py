from fastapi import FastAPI

# Core Findr routes
from api.routes.search import router as search_router
from api.routes.listings import router as listings_router
from api.routes.renderer import router as renderer_router
from api.routes.contract import router as contract_router
from api.routes.dialogue import router as dialogue_router
from api.routes.goals import router as goals_router
from api.routes.scene import router as scene_router
from api.routes.registry import router as registry_router

# WTCHR routes
from api.routes.wtchr import router as wtchr_router
from api.routes.wchtr_renderer import router as wchtr_renderer_router
from api.routes.wchtr_voice import router as wchtr_voice_router

# New global routes
from api.routes.voice import router as voice_router
from api.routes.evolution import router as evolution_router
from api.routes.trinn import router as trinn_router

app = FastAPI()

# Register core Findr routes
app.include_router(search_router)
app.include_router(listings_router)
app.include_router(renderer_router)
app.include_router(contract_router)
app.include_router(dialogue_router)
app.include_router(goals_router)
app.include_router(scene_router)
app.include_router(registry_router)

# Register WTCHR subsystem
app.include_router(wtchr_router)
app.include_router(wchtr_renderer_router)
app.include_router(wchtr_voice_router)

# Register new global engines
app.include_router(voice_router)
app.include_router(evolution_router)
app.include_router(trinn_router)
