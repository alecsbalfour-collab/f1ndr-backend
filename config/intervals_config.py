class IntervalsConfig:
    def __init__(self):
        self.HEARTBEAT_INTERVAL_SECONDS = 30
        self.CLEANUP_JOB_INTERVAL_SECONDS = 3600
        self.WATCHDOG_CHECK_INTERVAL_SECONDS = 60

intervals_config = IntervalsConfig()
