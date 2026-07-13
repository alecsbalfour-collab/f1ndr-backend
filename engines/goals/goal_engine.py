class GoalEngine:
    def __init__(self):
        self.goals = {}
        self.completed = []

    def create_goal(self, goal_id: str, description: str):
        self.goals[goal_id] = {
            "description": description,
            "progress": 0.0,
            "status": "active"
        }

    def update_progress(self, goal_id: str, progress: float):
        if goal_id not in self.goals:
            return False

        self.goals[goal_id]["progress"] = progress

        if progress >= 1.0:
            self.goals[goal_id]["status"] = "completed"
            self.completed.append(goal_id)

        return True

    def delete_goal(self, goal_id: str):
        if goal_id in self.goals:
            del self.goals[goal_id]
        if goal_id in self.completed:
            self.completed.remove(goal_id)

    def snapshot(self):
        return {
            "goals": self.goals,
            "completed": self.completed
        }
