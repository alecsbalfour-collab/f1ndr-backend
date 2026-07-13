class SceneContextEngine:
    def __init__(self):
        self.context = {
            "location": None,
            "time_of_day": None,
            "weather": None,
            "characters": [],
            "objects": [],
            "mood": "neutral"
        }

    def set_location(self, location: str):
        self.context["location"] = location

    def set_time_of_day(self, time: str):
        self.context["time_of_day"] = time

    def set_weather(self, weather: str):
        self.context["weather"] = weather

    def add_character(self, name: str):
        if name not in self.context["characters"]:
            self.context["characters"].append(name)

    def remove_character(self, name: str):
        if name in self.context["characters"]:
            self.context["characters"].remove(name)

    def add_object(self, obj: str):
        if obj not in self.context["objects"]:
            self.context["objects"].append(obj)

    def remove_object(self, obj: str):
        if obj in self.context["objects"]:
            self.context["objects"].remove(obj)

    def set_mood(self, mood: str):
        self.context["mood"] = mood

    def snapshot(self):
        return self.context
