class GoalService:
    def __init__(self):
        self._goals = []

    def get_all_goals(self):
        return self._goals

    def add_goal(self, goal: dict):
        self._goals.append(goal)
        return {"status": "added", "goal": goal}

    def delete_goal(self, goal_id: str):
        for g in self._goals:
            if g.get("id") == goal_id:
                self._goals.remove(g)
                return {"status": "deleted", "goal_id": goal_id}
        return {"status": "not_found", "goal_id": goal_id}
