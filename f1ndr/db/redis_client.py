import redis
from f1ndr.config.config import F1ndrConfig


def get_redis():
    """
    Create and return a Redis client for f1ndr.
    """
    return redis.Redis(
        host=F1ndrConfig.REDIS["host"],
        port=F1ndrConfig.REDIS["port"],
        decode_responses=True
    )
