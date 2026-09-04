# core/core/rules_core.py

def apply_rules(payload: dict) -> dict:
    """Apply core business rules."""
    cleaned = dict(payload)

    if "title" in cleaned and isinstance(cleaned["title"], str):
        cleaned["title"] = cleaned["title"].strip()

    return cleaned

def is_valid_title(title: str) -> bool:
    """Check if a title is valid."""
    return isinstance(title, str) and len(title.strip()) > 0
