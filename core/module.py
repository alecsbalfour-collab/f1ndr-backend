# core/module.py

from .config.settings_config import load_settings
from .core.rules_core import apply_rules
from .Data.environment_data import get_environment_data
from .Db.cache_db import get_cache
from .utils.helpers_utils import generate_id

def load_core_system() -> dict:
    """Load all core subsystems."""
    return {
        "config": load_settings(),
        "data": get_environment_data(),
        "db": get_cache(),
        "utils": {"id": generate_id()},
    }

def run_core_pipeline(payload: dict) -> dict:
    """Run the core rule pipeline."""
    return apply_rules(payload)
