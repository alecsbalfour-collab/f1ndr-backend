class PlatformsEngine:
    def __init__(self):
        self.registry = {
            "kijiji": {
                "enabled": True,
                "adapter": "kijiji",
                "categories": ["bicycles", "vehicles", "electronics"]
            },
            "craigslist": {
                "enabled": True,
                "adapter": "craigslist",
                "categories": ["bicycles", "vehicles"]
            },
            "facebook": {
                "enabled": False,
                "adapter": "facebook",
                "categories": ["bicycles", "vehicles"]
            }
        }

    def get_enabled(self):
        return [name for name, data in self.registry.items() if data["enabled"]]

    def get_platform(self, name):
        return self.registry.get(name, None)

    def filter_by_category(self, category):
        return [
            name for name, data in self.registry.items()
            if category in data["categories"] and data["enabled"]
        ]

    def run(self, payload):
        category = payload.get("category", "")
        enabled = self.get_enabled()
        filtered = self.filter_by_category(category)

        return {
            "enabled_platforms": enabled,
            "category_platforms": filtered
        }
