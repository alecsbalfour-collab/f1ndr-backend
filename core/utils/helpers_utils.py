# core/utils/helpers_utils.py

import uuid

def generate_id() -> str:
    """Generate a unique ID."""
    return str(uuid.uuid4())

def to_upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()
