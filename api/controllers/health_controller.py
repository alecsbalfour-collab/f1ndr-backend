from datetime import datetime


def get_health(version: str):
    return {
        "status": "ok",
        "version": version,
        "timestamp": datetime.utcnow().isoformat()
    }
