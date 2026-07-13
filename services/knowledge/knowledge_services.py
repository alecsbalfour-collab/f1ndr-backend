from engines.knowledge.knowledge_engine import KnowledgeEngine

class KnowledgeService:
    def __init__(self):
        self.engine = KnowledgeEngine()

    def add_fact(self, key: str, value: str, category: str = None):
        self.engine.add_fact(key, value, category)

    def remove_fact(self, key: str):
        self.engine.remove_fact(key)

    def get_fact(self, key: str):
        return self.engine.get_fact(key)

    def get_category(self, category: str):
        return self.engine.get_category(category)

    def snapshot(self):
        return self.engine.snapshot()
