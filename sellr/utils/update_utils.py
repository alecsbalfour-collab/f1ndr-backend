"""
Update utilities for Sellr.
"""

def can_partial_update(config: dict) -> bool:
    return config.get("allow_partial_updates", True)


def limit_update_batch(config: dict, count: int) -> bool:
    return count <= config.get("max_update_batch", 50)
