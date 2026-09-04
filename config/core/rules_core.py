# config/core/rules.py

CONFIG_RULES = {
    "allowed_sections": [
        "app",
        "database",
        "logging",
        "security",
        "performance"
    ],

    "required_keys": {
        "app": ["name", "version", "environment"],
        "database": ["host", "port", "username", "password", "name"],
        "logging": ["level", "format"],
        "security": ["enable_sandbox", "max_request_size"],
        "performance": ["cache_enabled", "max_workers"]
    }
}
