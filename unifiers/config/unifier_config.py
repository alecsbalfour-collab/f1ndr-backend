# f1ndr-backend/unifiers/config/unifier_config.py
"""
Config for Unifiers behavior.
"""

def get_unifier_config() -> dict:
    return {
        "enabled": True,
        "max_batch_size": 200,
        "strict_mode": True,
    }
