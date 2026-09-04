from scheduler.job_runner import JobRunner
from scheduler.config.scheduler_config import SCHEDULER_INTERVALS

def run_all_once():
    runner = JobRunner()
    for job_name in SCHEDULER_INTERVALS.keys():
        runner.run_job(job_name)

if __name__ == "__main__":
    run_all_once()
