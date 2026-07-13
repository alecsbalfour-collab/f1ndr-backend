from fastapi import APIRouter
from scheduler.cron import run_all

router = APIRouter()


@router.get("/status")
def scraper_status():
    return {"status": "ready", "message": "Scrapers are available"}


@router.post("/run")
def run_scrapers():
    try:
        run_all()
        return {"status": "success", "message": "Scrapers executed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
