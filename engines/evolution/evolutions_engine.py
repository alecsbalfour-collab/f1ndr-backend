import random

class EvolutionEngine:
    def __init__(self):
        self.state = {
            "traits": {},
            "experience": 0,
            "level": 1,
            "growth_log": []
        }

    def add_experience(self, amount: int):
        self.state["experience"] += amount
        self.state["growth_log"].append(f"Experience +{amount}")

        # Level-up logic
        while self.state["experience"] >= self._required_xp():
            self.state["experience"] -= self._required_xp()
            self.state["level"] += 1
            self.state["growth_log"].append(f"Level up → {self.state['level']}")

    def _required_xp(self):
        return 100 * self.state["level"]

    def evolve_trait(self, trait: str, delta: float):
        current = self.state["traits"].get(trait, 0.0)
        new_value = current + delta
        self.state["traits"][trait] = new_value
        self.state["growth_log"].append(f"Trait '{trait}' changed by {delta}")

    def snapshot(self):
        return self.state
