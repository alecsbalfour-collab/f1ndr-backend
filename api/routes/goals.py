from fastapi import APIRouter, HTTPException
from services.goals.goal_service import GoalService
from models.goals.goal_model import build_goal_contract

router = APIRouter()
goals = GoalService()

@router.post("/create")
def create_goal(payload: dict):
    goal_id = payload.get("id")
    description = payload.get("description")

    if not goal_id or not description:
        raise HTTPException(status_code=400, detail="id and description required")

    goals.create_goal(goal_id, description)
    return {"created": goal_id}

@router.post("/progress")
def update_progress(payload: dict):
    goal_id = payload.get("id")
    progress = payload.get("progress")

    if goal_id is None or progress is None:
        raise HTTPException(status_code=400, detail="id and progress required")

    ok = goals.update_progress(goal_id, float(progress))
    if not ok:
        raise HTTPException(status_code=404, detail="goal not found")

    return {"updated": goal_id, "progress": progress}

@router.post("/delete")
def delete_goal(payload: dict):
    goal_id = payload.get("id")
    if not goal_id:
        raise HTTPException(status_code=400, detail="id required")

    goals.delete_goal(goal_id)
    return {"deleted": goal_id}

@router.get("/contract")
def get_contract():
    return build_goal_contract(goals.snapshot())
