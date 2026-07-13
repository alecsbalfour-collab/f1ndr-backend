from engines.scene.scene_context_engine import SceneContextEngine

class SceneService:
    def __init__(self):
        self.engine = SceneContextEngine()

    def set_location(self, location: str):
        self.engine.set_location(location)

    def set_time_of_day(self, time: str):
        self.engine.set_time_of_day(time)

    def set_weather(self, weather: str):
        self.engine.set_weather(weather)

    def add_character(self, name: str):
        self.engine.add_character(name)

    def remove_character(self, name: str):
        self.engine.remove_character(name)

    def add_object(self, obj: str):
        self.engine.add_object(obj)

    def remove_object(self, obj: str):
        self.engine.remove_object(obj)

    def set_mood(self, mood: str):
        self.engine.set_mood(mood)

    def snapshot(self):
        return self.engine.snapshot()
