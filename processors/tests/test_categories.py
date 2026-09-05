from core.categories_core import CategoriesCore
from db.categories_db import categories_db
from config.categories_config import categories_config
from utils.logger_utils import logger_utils


def test_categories_upsert():
    core = CategoriesCore(categories_config, categories_db, logger_utils.logger)
    result = core.upsert_category({"name": "Test", "slug": "test"})
    assert result["slug"] == "test"
