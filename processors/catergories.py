from .config.categories_config import CategoriesConfig
from .core.categories_core import CategoriesCore
from .core.base_processor import BaseProcessor
from .db.categories_db import CategoriesDB


class CategoriesProcessor(BaseProcessor):
    def __init__(
        self,
        config: CategoriesConfig | None = None,
        db: CategoriesDB | None = None
    ):
        config = config or CategoriesConfig()
        core = CategoriesCore(config)
        db = db or CategoriesDB()

        super().__init__(config=config, core=core, db=db)

    def run(self, text: str):
        self.validate(text)
        categories = self.core.process(text)
        self.db.save(text, categories)
        return categories
