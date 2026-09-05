# f1ndr-backend/trinn/config/normalize_config.py
"""
Config for TRINN normalize stage.
"""

def get_normalize_config() -> dict:
    return {
        "enabled": True,
        "strict": True,
    }
