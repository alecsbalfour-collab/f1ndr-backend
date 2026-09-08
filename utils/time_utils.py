import time
from datetime import datetime, timezone
class TimeUtils:
    def __init__(self):
        pass
    def get_current_time(self):
        return datetime.now(timezone.utc)

time_utils = TimeUtils()
