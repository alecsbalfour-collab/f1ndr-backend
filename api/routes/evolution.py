from fastapi import APIRouter, HTTPException

router = APIRouter()

# Simple placeholder service logic
# (You can replace this with your real evolution engine later)
class EvolutionEngine:
    def __init__(self):
        self.state = {}

    def update(self, payload):
        self.state.update(payload)
        return self.state

    def get_state(self):
        return self.state


evolution = EvolutionEngine()


@router.post("/evolution/update")
def evolution_update(payload: dict):
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Payload must be a dictionary")
    new_state = evolution.update(payload)
    return {"updated": new_state}


@router.get("/evolution/state")
def evolution_state():
    return {"state": evolution.get_state()}
