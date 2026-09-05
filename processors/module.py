from core.base_processor import BaseProcessor
from core.categories_core import CategoriesCore
from core.normalize_core import NormalizeCore

from config.base_config import base_config
from config.categories_config import categories_config
from config.normalize_config import normalize_config

from db.categories_db import categories_db
from db.normalize_db import normalize_db
from db.mongo_client import mongo_client

from utils.logger_utils import logger_utils
from utils.validation_utils import validation_utils
from utils.exception_utils import exception_utils
from utils.formatter_utils import formatter_utils


def build_processors_module():
    base = BaseProcessor(
        base_config=base_config,
        logger=logger_utils.logger,
        validator=validation_utils,
        exceptions=exception_utils,
        formatter=formatter_utils,
    )

    categories = CategoriesCore(
        config=categories_config,
        db=categories_db,
        logger=logger_utils.logger,
    )

    normalize = NormalizeCore(
        config=normalize_config,
        db=normalize_db,
        logger=logger_utils.logger,
    )

    return {
        "base": base,
        "categories": categories,
        "normalize": normalize,
        "mongo_client": mongo_client,
    }


processors = build_processors_module()
