from engines.evolution.evolution_engine import EvolutionEngine

class EvolutionService:
    def __init__(self):
        self.engine = EvolutionEngine()

    def add_experience(self, amount: int):
        self.engine.add_experience(amount)

    def evolve_trait(self, trait: str, delta: float):
        self.engine.evolve_trait(trait, delta)

    def snapshot(self):
        return self.engine.snapshot()
