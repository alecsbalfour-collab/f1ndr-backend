# services/trinn_events.py

class TrinnEvents:
    def __init__(self, controller):
        self.controller = controller

    def on_focus(self):
        self.controller.set_state("focused")

    def on_relax(self):
        self.controller.set_state("relaxed")

    def on_play(self):
        self.controller.set_state("playful")

    def on_idle(self):
        self.controller.set_state("neutral")
