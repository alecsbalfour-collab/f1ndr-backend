class SchedulerConfig:
    def defaults(self) -> dict:
        return {
            "enabled": True,
            "max_jobs": 10,
        }


scheduler_config = SchedulerConfig()
