from utils.logger_utils import logger_utils


def test_logger_utils_has_logger():
    assert logger_utils.logger is not None
