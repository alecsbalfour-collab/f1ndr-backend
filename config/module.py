# config/module.py

from .core.rules import CONFIG_RULES
from .data.environment import ENV
from .utils.loader import load_config
from .db.cache import config_cache

def get_config(section: str):
    """
    Global configuration entry point.
    Loads and caches configuration sections.
    """
    cached = config_cache.get(section)
    if cached:
        return cached

    config = load_config(section, CONFIG_RULES, ENV)
    config_cache.set(section, config)
    return config
