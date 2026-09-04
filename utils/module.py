# utils/module.py

from .core.rules import UTILS_RULES
from .utils.helpers import clean_text, safe_int, safe_float
from .db.cache import utils_cache

def normalize(value):
    """
    Root-level normalization entry point.
    Applies global utility rules.
    """
    if isinstance(value, str) and UTILS_RULES.get("trim_strings"):
        value = value.strip()

    if isinstance(value, str) and UTILS_RULES.get("collapse_spaces"):
        value = " ".join(value.split())

    return value
