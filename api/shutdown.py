from logging import getLogger

logger = getLogger("api.shutdown")

async def on_shutdown():
    """
    Shutdown hook for cleanup.
    Extend later with DB disconnects, cache flushes, etc.
    """
    logger.info("Application shutdown complete")
