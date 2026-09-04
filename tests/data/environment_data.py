# tests/Data/environment_data.py

def get_environment_data() -> dict:
    """Provide environment metadata for tests layer."""
    return {
        "layer": "tests",
        "mode": "local",
    }


def enrich_environment_data(env: dict) -> dict:
    env["meta"] = "tests-environment"
    return env
