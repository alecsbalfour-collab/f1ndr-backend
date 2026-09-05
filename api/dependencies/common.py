from fastapi import Depends
from config import get_settings

def get_app_settings():
    """
    Shared dependency for injecting settings into routes/controllers.
    """
    return get_settings()
