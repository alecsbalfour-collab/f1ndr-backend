# tests/config/settings_config.py

def load_tests_settings() -> dict:
    """Load test-layer configuration."""
    return {
        "TEST_ENV": "local",
        "TEST_DEBUG": True,
        "VERSION": "1.0.0",
    }


def validate_tests_settings(cfg: dict) -> bool:
    return "TEST_ENV" in cfg and "TEST_DEBUG" in cfg
