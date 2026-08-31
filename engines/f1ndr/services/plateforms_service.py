from engines.f1ndr.platforms_engine import PlatformsEngine

class PlatformsService:
    def __init__(self):
        self.engine = PlatformsEngine()

    def get_platforms(self, category: str):
        return self.engine.get_platforms(category)
