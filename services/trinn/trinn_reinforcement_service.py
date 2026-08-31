# trinn/services/trinn_reinforcement_service.py

class TrinnReinforcementService:
    def __init__(self):
        self.reward = 0
        self.last_action = None

    def apply_reward(self, value: int):
        self.reward += value

    def set_last_action(self, action: str):
        self.last_action = action

    def snapshot(self):
        return {
            "reward": self.reward,
            "last_action": self.last_action
        }
