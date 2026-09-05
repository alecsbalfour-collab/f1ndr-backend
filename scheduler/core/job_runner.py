class JobRunner:
    def __init__(self, metadata, logger, retry_utils):
        self.metadata = metadata
        self.logger = logger
        self.retry_utils = retry_utils

    def run_job(self, job_name: str, payload: dict) -> dict:
        self.logger.info(f"Running job: {job_name}")

        job_info = self.metadata.get(job_name)
        if not job_info:
            self.logger.error(f"Unknown job: {job_name}")
            return {"status": "error", "message": "unknown job"}

        return self.retry_utils.execute(job_info["handler"], payload)
