class RendererEngine:
    def __init__(self):
        self.state = {
            "scene": None,
            "animation": None,
            "dialogue": None,
            "voice": None,
            "characters": None
        }

    def bind_scene(self, scene_contract):
        self.state["scene"] = scene_contract

    def bind_animation(self, animation_contract):
        self.state["animation"] = animation_contract

    def bind_dialogue(self, dialogue_contract):
        self.state["dialogue"] = dialogue_contract

    def bind_voice(self, voice_contract):
        self.state["voice"] = voice_contract

    def bind_characters(self, registry_contract):
        self.state["characters"] = registry_contract

    def snapshot(self):
        return self.state
