from engines.wchtr.renderer_engine import RendererEngine

class RendererService:
    def __init__(self):
        self.engine = RendererEngine()

    def bind_scene(self, scene_contract):
        self.engine.bind_scene(scene_contract)

    def bind_animation(self, animation_contract):
        self.engine.bind_animation(animation_contract)

    def bind_dialogue(self, dialogue_contract):
        self.engine.bind_dialogue(dialogue_contract)

    def bind_voice(self, voice_contract):
        self.engine.bind_voice(voice_contract)

    def bind_characters(self, registry_contract):
        self.engine.bind_characters(registry_contract)

    def snapshot(self):
        return self.engine.snapshot()
