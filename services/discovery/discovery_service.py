from engines.discovery.discovery_engine import DiscoveryEngine

class DiscoveryService:
    def __init__(self):
        self.engine = DiscoveryEngine()

    def process(self, payload):
        return self.engine.run(payload)
