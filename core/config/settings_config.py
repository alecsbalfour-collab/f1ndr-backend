# core/config/settings_config.py

import os

def load_settings() -> dict:
    """Load environment-based configuration."""
    return {
        "ENV": os.getenv("F1NDR_ENV", "dev"),
        "DEBUG": os.getenv("F1NDR_DEBUG", "false").lower() == "true",
        "VERSION": "1.0.0",
    }

def validate_settings(cfg: dict) -> bool:
    """Validate core settings."""
    return "ENV" in cfg and "DEBUG" in cfg
