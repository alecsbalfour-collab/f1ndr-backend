import os
class SchedulerConfig:
    def __init__(self):
        self.ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
        self.MAX_WORKERS = 5
        self.DAEMON_MODE = True
        self.LOG_LEVEL = "INFO"

scheduler_config = SchedulerConfig()
