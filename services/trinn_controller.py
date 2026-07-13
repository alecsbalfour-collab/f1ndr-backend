from services.trinn_state_machine import TrinnStateMachine
from services.trinn_memory_service import TrinnMemoryService
from services.trinn_dialogue_service import TrinnDialogueService
from services.trinn_animation_engine import TrinnAnimationEngine
from models.trinn_contract import build_trinn_contract

class TrinnController:
    def __init__(self):
        self.machine = TrinnStateMachine()
        self.memory = TrinnMemoryService()
        self.dialogue = TrinnDialogueService()
        self.animation = TrinnAnimationEngine()

    def set_state(self, state):
        self.machine.set_state(state)
        self.animation.apply_state(state)
        self.animation.build_timeline(state)

    def get_snapshot(self):
        return self.machine.snapshot()

    def get_contract(self, emotion, reinforcement):
        snapshot = self.machine.snapshot()
        memory_snapshot = self.memory.snapshot()
        personality = self.dialogue.get_personality()
        animation_snapshot = self.animation.snapshot()

        return build_trinn_contract(
            snapshot,
            memory_snapshot,
            personality,
            emotion,
            reinforcement,
            animation_snapshot
        )
