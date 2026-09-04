# tests/module.py

from .config.settings_config import load_tests_settings
from .core.rules_core import apply_tests_rules
from .Data.environment_data import get_environment_data
from .Db.connection_db import get_tests_connection
from .utils.helpers_utils import generate_tests_id


def load_tests_system() -> dict:
    """Load all test-layer subsystems."""
    return {
        "config": load_tests_settings(),
        "environment": get_environment_data(),
        "connection": get_tests_connection(),
        "utils": {"id": generate_tests_id()},
    }


def run_tests_pipeline(payload: dict) -> dict:
    """Run test-layer rule pipeline."""
    return apply_tests_rules(payload)
