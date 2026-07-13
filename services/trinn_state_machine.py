from logic.trinn import Trinn

class TrinnStateMachine:
    def __init__(self):
        self.trinn = Trinn()

    def get_state(self):
        return self.trinn.get_state()

    def set_state(self, new_state):
        return self.trinn.set_state(new_state)

    def interact(self, text):
        return self.trinn.interact(text)

    def get_profile(self):
        return self.trinn.get_profile()
