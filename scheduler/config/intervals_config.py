class IntervalsConfig:
    def defaults(self) -> dict:
        return {
            "heartbeat_interval": 30,
            "watchdog_interval": 60,
            "job_interval": 120,
        }


intervals_config = IntervalsConfig()
