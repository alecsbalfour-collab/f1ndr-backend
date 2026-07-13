import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("trinn")
from utils.logger import logger

def set_state(self, state: str):
    logger.info(f"Trinn state changed to: {state}")
    self.machine.set_state(state)
