from core.utils.errors import ValidationError

def validate_query(query: str):
    if not query or len(query.strip()) == 0:
        raise ValidationError("Search query cannot be empty.")
    return True

def validate_platforms(platforms: list[str] | None):
    if platforms is None:
        return True
    if not isinstance(platforms, list):
        raise ValidationError("Platforms must be a list.")
    return True
