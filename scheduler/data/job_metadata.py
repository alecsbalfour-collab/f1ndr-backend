JOB_METADATA = {
    "cleanup": {
        "handler": lambda payload: {"status": "ok", "cleaned": True},
    },
    "sync": {
        "handler": lambda payload: {"status": "ok", "synced": True},
    },
}
