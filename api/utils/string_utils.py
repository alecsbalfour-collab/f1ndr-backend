def to_lower(value: str) -> str:
    """
    Convert a string to lowercase safely.
    """
    return value.lower() if isinstance(value, str) else value


def to_upper(value: str) -> str:
    """
    Convert a string to uppercase safely.
    """
    return value.upper() if isinstance(value, str) else value


def strip_spaces(value: str) -> str:
    """
    Remove leading/trailing whitespace.
    """
    return value.strip() if isinstance(value, str) else value
