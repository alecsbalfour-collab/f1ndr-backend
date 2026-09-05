from core.normalize_core import NormalizeCore
from db.normalize_db import normalize_db
from config.normalize_config import normalize_config
from utils.logger_utils import logger_utils


def test_normalize_payload():
    core = NormalizeCore(normalize_config, normalize_db, logger_utils.logger)
    result = core.normalize({"field": " value "})
    assert result["field"] == "value"
