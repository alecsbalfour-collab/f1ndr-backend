# core/Data/environment_data.py

def get_environment_data() -> dict:
    """Provide static data context."""
    return {
        "region": "us",
        "timezone": "UTC",
        "app": "f1ndr",
    }

def enrich_context(ctx: dict) -> dict:
    """Add metadata to context."""
    ctx["meta"] = "core-data"
    return ctx
