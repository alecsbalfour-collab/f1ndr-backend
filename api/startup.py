from logging import getLogger

logger = getLogger("api.startup")

async def on_startup():
    """
    Startup hook for initializing resources.
    Extend later with DB connections, caches, etc.
    """
    logger.info("Application startup complete")
