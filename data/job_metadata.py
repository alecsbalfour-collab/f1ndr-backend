JOB_METADATA = {
    "cleanup_job": {
        "handler": "pipelines.cleanup_pipeline",
        "coalesce": True,
        "misfire_grace_time": 60
    },
    "ingestion_replay": {
        "handler": "pipelines.ingestion_history",
        "coalesce": False,
        "misfire_grace_time": 120
    }
}
