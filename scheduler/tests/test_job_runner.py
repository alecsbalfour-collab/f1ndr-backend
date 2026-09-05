from core.job_runner import JobRunner
from data.job_metadata import JOB_METADATA
from utils.retry_utils import retry_utils
from utils.scheduler_logger_utils import scheduler_logger_utils


def test_job_runner():
    runner = JobRunner(JOB_METADATA, scheduler_logger_utils.logger, retry_utils)
    result = runner.run_job("cleanup", {})
    assert result["status"] == "ok"
