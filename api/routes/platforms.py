from fastapi import APIRouter
from db.platforms import (
    get_all_platforms,
    get_platform,
    register_platform,
    mark_success,
    mark_failure,
)

router = APIRouter()


@router.get("/")
def list_platforms():
    """
    Return all registered platforms.
    """
    return {"status": "ok", "platforms": get_all_platforms()}


@router.get("/{name}")
def get_single_platform(name: str):
    """
    Return a single platform by name.
    """
    platform = get_platform(name)
    if not platform:
        return {"status": "error", "message": "Platform not found"}
    return {"status": "ok", "platform": platform}


@router.post("/register")
def register_new_platform(name: str, url: str, scraper: str, category: str = "unknown"):
    """
    Register a new platform into the system.
    """
    register_platform(name, url, scraper, category)
    return {"status": "ok", "message": f"Platform '{name}' registered"}


@router.post("/{name}/success")
def mark_platform_success(name: str):
    """
    Mark a platform scraper run as successful.
    """
    mark_success(name)
    return {"status": "ok", "message": f"Platform '{name}' marked successful"}


@router.post("/{name}/failure")
def mark_platform_failure(name: str, error: str):
    """
    Mark a platform scraper run as failed.
    """
    mark_failure(name, error)
    return {"status": "ok", "message": f"Platform '{name}' marked failed"}

