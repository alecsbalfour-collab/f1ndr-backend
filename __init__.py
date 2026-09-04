import datetime
import json
import os

DEBUG_ENABLED = os.getenv("F1NDR_DEBUG", "false").lower() == "true"


def debug(message: str, payload: dict | None = None) -> None:
    """
    Global debugger for the entire f1ndr-backend.
    Structured JSON logging, environment-controlled.
    """
    if not DEBUG_ENABLED:
        return

    timestamp = datetime.datetime.utcnow().isoformat()

    log = {
        "timestamp": timestamp,
        "message": message,
    }

    if payload is not None:
        try:
            log["payload"] = payload
        except Exception:
            log["payload"] = str(payload)

    print("[F1NDR DEBUG]", json.dumps(log, indent=2))
