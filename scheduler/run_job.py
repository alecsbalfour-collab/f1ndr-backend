import sys
from scheduler.job_runner import JobRunner

if __name__ == "__main__":
    job = sys.argv[1]
    runner = JobRunner()
    runner.run_job(job)
