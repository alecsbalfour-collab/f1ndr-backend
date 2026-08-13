from fastapi import APIRouter, HTTPException
from services.goals.goal_service import GoalService
from models.goals.goal_model import GoalRequest

router = APIRouter()
service = GoalService()


@router.post("/goals")
def generate_goals(payload: GoalRequest):
    """
    Generate goals using the existing GoalService.
    This wires the route → service → engine → model exactly as your architecture intends.
    """

    try:
        result = service.generate_goals(payload)

        return {
            "status": "success",
            "engine": "goals",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
