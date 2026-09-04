from processors.data.categories_data import CATEGORY_KEYWORDS


class CategoriesCore:
    """
    Core categorization logic.
    Uses keyword matching and rule engine.
    """

    def __init__(self, config):
        self.config = config

    def process(self, text: str) -> list:
        categories = set()
        lowered = text.lower()

        if self.config.enable_keyword_matching:
            for category, keywords in CATEGORY_KEYWORDS.items():
                if any(keyword in lowered for keyword in keywords):
                    categories.add(category)

        if self.config.enable_rule_engine:
            if len(text) >= self.config.min_length_for_long_text:
                categories.add("long_text")

        return sorted(categories)
