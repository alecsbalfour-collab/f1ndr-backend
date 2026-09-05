# f1ndr-backend/unifiers/config/normalize_config.py
"""
Config for Unifiers normalize stage.
"""

def get_normalize_config() -> dict:
    return {
        "enabled": True,
        "trim_titles": True,
        "default_platform": "unified",
    }
