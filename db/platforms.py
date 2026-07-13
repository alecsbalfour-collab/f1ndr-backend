from datetime import datetime
from db.mongo import get_platforms_collection


def register_platform(name, url, scraper, category="unknown"):
    """
    Create or update a platform entry.
    """
    col = get_platforms_collection()

    col.update_one(
        {"name": name},
        {
            "$set": {
                "name": name,
                "url": url,
                "scraper": scraper,
                "category": category,
                "status": "ready",
                "last_run": None,
                "success_count": 0,
                "failure_count": 0,
                "last_error": None,
                "updated_at": datetime.utcnow(),
            }
        },
        upsert=True,
    )


def mark_success(name):
    """
    Mark a successful scraper run.
    """
    col = get_platforms_collection()

    col.update_one(
        {"name": name},
        {
            "$set": {"last_run": datetime.utcnow(), "status": "ok"},
            "$inc": {"success_count": 1},
        },
    )


def mark_failure(name, error_msg):
    """
    Mark a failed scraper run.
    """
    col = get_platforms_collection()

    col.update_one(
        {"name": name},
        {
            "$set": {
                "last_run": datetime.utcnow(),
                "status": "error",
                "last_error": error_msg,
            },
            "$inc": {"failure_count": 1},
        },
    )


def get_all_platforms():
    """
    Return all registered platforms.
    """
    col = get_platforms_collection()
    return list(col.find())


def get_platform(name):
    """
    Return a single platform entry.
    """
    col = get_platforms_collection()
    return col.find_one({"name": name})
