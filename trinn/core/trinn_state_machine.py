# trinn/trinn_state_machine.py

class TrinnStateMachine:
    def __init__(self):
        self.state = "neutral"

        self.transitions = {
            "neutral": ["focused", "relaxed", "playful"],
            "focused": ["neutral", "relaxed"],
            "relaxed": ["neutral", "playful"],
            "playful": ["neutral", "focused"]
        }

    def can_transition(self, new_state):
        return new_state in self.transitions.get(self.state, [])

    def transition(self, new_state):
        if self.can_transition(new_state):
            self.state = new_state
        return self.state
