"""
Diff utilities for watchr.
Used to detect changes between old and new listing data.
"""

from typing import Dict, Any


def diff_dict(old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return a dict of changed fields.
    """
    changes = {}

    for key, old_val in old.items():
        new_val = new.get(key)
        if new_val != old_val:
            changes[key] = {"old": old_val, "new": new_val}

    return changes
