from engines.categories.categories_engine import CategoriesEngine

class CategoriesService:
    def __init__(self):
        self.engine = CategoriesEngine()

    def process(self, payload):
        return self.engine.run(payload)
