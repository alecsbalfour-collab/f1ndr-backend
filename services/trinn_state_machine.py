from fastapi import APIRouter

from logic.trinn import Trinn
from services.trinn_appearance_service import TrinnAppearanceService
from services.trinn_behavior_service import TrinnBehaviorService

router = APIRouter()

# Core profile
trinn = Trinn()
appearance_service = TrinnAppearanceService()
behavior_service = TrinnBehaviorService()


# ─────────────────────────────────────────────
# BASE PROFILE
# ─────────────────────────────────────────────
@router.get("/trinn")
def get_trinn_profile():
    return trinn.get_profile()


# ─────────────────────────────────────────────
# APPEARANCE ENGINE
# ─────────────────────────────────────────────
@router.get("/trinn/appearance")
def get_trinn_appearance():
    return appearance_service.get_appearance()

@router.get("/trinn/appearance/stateful")
def get_trinn_stateful_appearance():
    return appearance_service.get_stateful_appearance()

@router.post("/trinn/appearance/state/{state}")
def set_trinn_appearance_state(state: str):
    appearance_service.set_state(state)
    return {"state": state}


# ─────────────────────────────────────────────
# BEHAVIOR ENGINE
# ─────────────────────────────────────────────
@router.get("/trinn/behavior")
def get_trinn_behavior():
    return behavior_service.get_behavior()

@router.post("/trinn/behavior/state/{state}")
def set_trinn_behavior_state(state: str):
    behavior_service.set_state(state)
    return {"state": state}
