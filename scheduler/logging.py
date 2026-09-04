import logging
from logging.handlers import RotatingFileHandler
import os

os.makedirs("logs", exist_ok=True)

handler = RotatingFileHandler(
    "logs/scheduler.log",
    maxBytes=5_000_000,
    backupCount=5
)

logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("scheduler")
