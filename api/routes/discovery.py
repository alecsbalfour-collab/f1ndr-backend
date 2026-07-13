from fastapi import APIRouter
from discovery.run import run_discovery
from db.mongo import get_discovery_collection

router = APIRouter()


@router.get("/sites")
def list_discovered_sites():
    col = get_discovery_collection()
    sites = list(col.find())
    for s in sites:
        s["_id"] = str(s["_id"])
    return sites


@router.post("/scan")
def scan_for_new_sites():
    created = run_discovery()
    return {"status": "completed", "created_files": created}
