# config/utils/loader.py

import os

def load_env(key: str, default=None, cast=str):
    """
    Safely load an environment variable with optional casting.
    """
    value = os.getenv(key, default)
    try:
        return cast(value)
    except Exception:
        return default


def load_section(section: str, rules: dict, env: dict) -> dict:
    """
    Load a configuration section using rule definitions and environment values.
    Validates required keys and returns a structured config dict.
    """
    if section not in rules["allowed_sections"]:
        raise ValueError(f"Unknown config section: {section}")

    required_keys = rules["required_keys"].get(section, [])
    config = {}

    # Map environment variables into structured config
    if section == "app":
        config = {
            "name": env["APP_NAME"],
            "version": env["APP_VERSION"],
            "environment": env["ENVIRONMENT"]
        }

    elif section == "database":
        config = {
            "host": env["DB_HOST"],
            "port": env["DB_PORT"],
            "username": env["DB_USER"],
            "password": env["DB_PASS"],
            "name": env["DB_NAME"]
        }

    elif section == "logging":
        config = {
            "level": env["LOG_LEVEL"],
            "format": env["LOG_FORMAT"]
        }

    elif section == "security":
        config = {
            "enable_sandbox": env["SEC_SANDBOX"],
            "max_request_size": env["SEC_MAX_REQ"]
        }

    elif section == "performance":
        config = {
            "cache_enabled": env["PERF_CACHE"],
            "max_workers": env["PERF_WORKERS"]
        }

    # Validate required keys
    missing = [key for key in required_keys if key not in config]
    if missing:
        raise RuntimeError(f"Missing required config keys: {missing}")

    return config


def load_config(section: str, rules: dict, env: dict) -> dict:
    """
    Public loader used by config/module.py.
    """
    return load_section(section, rules, env)
