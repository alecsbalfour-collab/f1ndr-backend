class CategoriesCore:
    def __init__(self, config, db, logger):
        self.config = config
        self.db = db
        self.logger = logger

    def upsert_category(self, category: dict) -> dict:
        self.logger.info(f"Upserting category: {category.get('name')}")
        return self.db.upsert(category)

    def list_categories(self) -> list:
        self.logger.info("Listing categories")
        return self.db.list_all()
