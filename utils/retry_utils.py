import time
class RetryUtils:
    def __init__(self):
        pass
    def execute_with_retry(self, func, retries=3, delay=1, *args, **kwargs):
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if i == retries - 1:
                    raise e
                time.sleep(delay)

retry_utils = RetryUtils()
