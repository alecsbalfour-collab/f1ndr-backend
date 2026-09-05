# f1ndr-backend/unifiers/config/transform_config.py
"""
Config for Unifiers transform stage.
"""

def get_transform_config() -> dict:
    return {
        "enabled": True,
        "allow_custom_mappings": True,
    }
