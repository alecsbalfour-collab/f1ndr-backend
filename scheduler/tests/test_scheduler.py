from core.scheduler_core import SchedulerCore
from config.scheduler_config import scheduler_config
from config.intervals_config import intervals_config
from db.scheduler_state import scheduler_state
from db.scheduler_history import scheduler_history
from utils.scheduler_logger_utils import scheduler_logger_utils
from utils.time_utils import time_utils


def test_scheduler_tick():
    scheduler = SchedulerCore(
        scheduler_config,
        intervals_config,
        scheduler_state,
        scheduler_history,
        scheduler_logger_utils.logger,
        time_utils,
    )

    result = scheduler.tick()
    assert result["status"] == "ok"
