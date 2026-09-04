import time
import importlib
from scheduler.logging import logger

class JobRunner:
    """
    Loads and executes jobs dynamically.
    Tracks last run timestamps.
    """

    def __init__(self):
        self.last_run = {}

    def run_if_due(self, job_name, interval):
        now = time.time()
        last = self.last_run.get(job_name, 0)

        if now - last >= interval:
            self.last_run[job_name] = now
            self.run_job(job_name)

    def run_job(self, job_name):
        logger.info(f"Running job: {job_name}")

        try:
            module = importlib.import_module(f"scheduler.jobs.{job_name}")
            module.run()
        except Exception as e:
            logger.error(f"Job {job_name} failed: {e}")

        logger.info(f"Completed job: {job_name}")
