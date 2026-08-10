from fastapi import APIRouter
from .f1ndr import router as f1ndr_router

router = APIRouter()

router.include_router(f1ndr_router)
