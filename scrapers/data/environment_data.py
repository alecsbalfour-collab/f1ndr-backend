def get_environment_data() -> dict:
    return {
        "layer": "scraper",
        "region": "us",
        "timezone": "UTC",
    }

def enrich_environment_data(env: dict) -> dict:
    env["meta"] = "scraper-environment"
    return env
