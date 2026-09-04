import os

def load_db_settings():
    return {
        "db_host": os.getenv("DB_HOST", "localhost"),
        "db_port": int(os.getenv("DB_PORT", "27017")),
        "db_name": os.getenv("DB_NAME", "f1ndr"),
        "db_user": os.getenv("DB_USER", None),
        "db_pass": os.getenv("DB_PASS", None),
    }

def validate_db_settings(settings: dict):
    if not settings.get("db_host"):
        raise ValueError("DB_HOST is required")

    if not settings.get("db_port"):
        raise ValueError("DB_PORT is required")

    if not settings.get("db_name"):
        raise ValueError("DB_NAME is required")

    return True
