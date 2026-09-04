# tests/core/rules_core.py

def apply_tests_rules(record: dict) -> dict:
    """Apply test-layer rules."""
    cleaned = dict(record)
    cleaned["tested"] = True
    return cleaned


def is_valid_tests_record(record: dict) -> bool:
    """Validate a test-layer record."""
    return isinstance(record, dict)
