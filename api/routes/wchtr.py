from fastapi import APIRouter

router = APIRouter()

@router.get("/wchtr/status")
def wchtr_status():
    return {"status": "ok", "module": "wchtr"}


