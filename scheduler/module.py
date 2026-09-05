from core.scheduler_core import SchedulerCore
from core.job_runner import JobRunner
from core.heartbeat import Heartbeat
from core.watchdog import Watchdog

from config.scheduler_config import scheduler_config
from config.intervals_config import intervals_config

from db.scheduler_state import scheduler_state
from db.scheduler_history import scheduler_history

from utils.scheduler_logger_utils import scheduler_logger_utils
from utils.retry_utils import retry_utils
from utils.time_utils import time_utils

from data.scheduler_data import SCHEDULER_DATA
from data.job_metadata import JOB_METADATA


def build_scheduler_module():
    scheduler = SchedulerCore(
        config=scheduler_config,
        intervals=intervals_config,
        state=scheduler_state,
        history=scheduler_history,
        logger=scheduler_logger_utils.logger,
        time_utils=time_utils,
    )

    runner = JobRunner(
        metadata=JOB_METADATA,
        logger=scheduler_logger_utils.logger,
        retry_utils=retry_utils,
    )

    heartbeat = Heartbeat(
        logger=scheduler_logger_utils.logger,
        state=scheduler_state,
        time_utils=time_utils,
    )

    watchdog = Watchdog(
        logger=scheduler_logger_utils.logger,
        state=scheduler_state,
        history=scheduler_history,
    )

    return {
        "scheduler": scheduler,
        "runner": runner,
        "heartbeat": heartbeat,
        "watchdog": watchdog,
        "state": scheduler_state,
        "history": scheduler_history,
    }


scheduler = build_scheduler_module()
