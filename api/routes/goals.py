from fastapi import APIRouter
from services.goals.goal_service import GoalService

router = APIRouter()
goals = GoalService()

@router.get("/goals")
def get_goals():
    return goals.get_all_goals()

@router.post("/goals")
def add_goal(goal: dict):
    return goals.add_goal(goal)

@router.delete("/goals/{goal_id}")
def delete_goal(goal_id: str):
    return goals.delete_goal(goal_id)
