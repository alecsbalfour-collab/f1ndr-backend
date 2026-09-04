import time
from scheduler.job_runner import JobRunner
from scheduler.config.scheduler_config import SCHEDULER_INTERVALS
from scheduler.logging import logger

class Scheduler:
    """
    Global scheduler for f1ndr backend.
    Runs recurring jobs based on configured intervals.
    """

    def __init__(self):
        self.runner = JobRunner()

    def start(self):
        logger.info("Scheduler started.")
        while True:
            for job_name, interval in SCHEDULER_INTERVALS.items():
                self.runner.run_if_due(job_name, interval)
            time.sleep(1)
