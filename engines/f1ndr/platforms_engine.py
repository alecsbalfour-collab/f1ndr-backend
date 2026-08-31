class PlatformsEngine:
    def get_platforms(self, category: str):
        mapping = {
            "bikes": ["kijiji", "facebook", "marketplace"],
            "vehicles": ["autotrader", "kijiji"],
            "pets": ["kijiji", "adoptapet"],
            "general": ["kijiji", "facebook", "ebay"]
        }
        return mapping.get(category, [])
