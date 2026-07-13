def build_goal_contract(snapshot):
    return {
        "goals": snapshot["goals"],
        "completed": snapshot["completed"],
        "meta": {
            "engine": "GoalEngine",
            "contract_type": "goal_system"
        }
    }
