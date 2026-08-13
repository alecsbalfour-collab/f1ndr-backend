from engines.platforms.platforms_engine import PlatformsEngine

class PlatformsService:
    def __init__(self):
        self.engine = PlatformsEngine()

    def process(self, payload):
        return self.engine.run(payload)
