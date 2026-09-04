def safe_lower(value: str | None):
    """
    Safely lowercase a string without throwing errors.
    """
    if not value:
        return ""
    return value.lower()


def safe_strip(value: str | None):
    """
    Safely strip whitespace from a string.
    """
    if not value:
        return ""
    return value.strip()
