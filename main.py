from fastapi import FastAPI

# ─────────────────────────────────────────────
# ROUTER IMPORTS
# ─────────────────────────────────────────────

# Trinn Intelligence Stack
from api.routes.trinn import router as trinn_router

# Multi‑Character Registry
from api.routes.registry import router as registry_router

# Scene Engine (will exist soon)
from api.routes.scene import router as scene_router

# Animation Engine (will exist soon)
from api.routes.animation import router as animation_router

# Dialogue Engine (LLM layer will exist soon)
from api.routes.dialogue import router as dialogue_router

# Evolution Engine (long‑term growth)
from api.routes.evolution import router as evolution_router

# Knowledge Engine (facts/world model)
from api.routes.knowledge import router as knowledge_router

# Goal/Task Engine
from api.routes.goals import router as goals_router

# f1ndr Search Engine
from api.routes.f1ndr import router as f1ndr_router

# wchtr App API
from api.routes.wchtr import router as wchtr_router

from api.routes.wchtr_renderer import router as renderer_router


# ─────────────────────────────────────────────
# FASTAPI APP
# ─────────────────────────────────────────────

app = FastAPI(
    title="watcHr Platform Backend",
    version="1.0.0",
    description="Unified enterprise backend powering Trinn, f1ndr, and wchtr."
)


# ─────────────────────────────────────────────
# ROUTER REGISTRATION
# ─────────────────────────────────────────────

app.include_router(trinn_router, prefix="/api/trinn")
app.include_router(registry_router, prefix="/api/registry")
app.include_router(scene_router, prefix="/api/scene")
app.include_router(animation_router, prefix="/api/animation")
app.include_router(dialogue_router, prefix="/api/dialogue")
app.include_router(evolution_router, prefix="/api/evolution")
app.include_router(knowledge_router, prefix="/api/knowledge")
app.include_router(goals_router, prefix="/api/goals")
app.include_router(f1ndr_router, prefix="/api/f1ndr")
app.include_router(wchtr_router, prefix="/api/wchtr")
app.include_router(renderer_router, prefix="/api/render")


# ─────────────────────────────────────────────
# ROOT ENDPOINT
# ─────────────────────────────────────────────

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "watcHr unified backend is running.",
