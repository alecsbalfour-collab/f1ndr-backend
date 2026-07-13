class KnowledgeEngine:
    def __init__(self):
        self.facts = {}
        self.categories = {}

    def add_fact(self, key: str, value: str, category: str = None):
        self.facts[key] = value

        if category:
            if category not in self.categories:
                self.categories[category] = []
            self.categories[category].append(key)

    def remove_fact(self, key: str):
        if key in self.facts:
            del self.facts[key]

        for cat in self.categories.values():
            if key in cat:
                cat.remove(key)

    def get_fact(self, key: str):
        return self.facts.get(key)

    def get_category(self, category: str):
        return {
            "category": category,
            "facts": {key: self.facts[key] for key in self.categories.get(category, [])}
        }

    def snapshot(self):
        return {
            "facts": self.facts,
            "categories": self.categories
        }
