import os


def get_db_environment():
    """
    Returns the current database environment.
    Used to switch DB configs between dev, staging, and production.
    """

    env = os.getenv("DB_ENV", "dev").lower()

    if env not in ["dev", "staging", "prod"]:
        env = "dev"

    return env
