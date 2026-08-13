from fastapi import APIRouter, HTTPException
from services.categories.categories_service import CategoriesService
from models.categories.categories_model import CategoriesRequest

router = APIRouter()
service = CategoriesService()

@router.post("/categories")
def categories(payload: CategoriesRequest):
    try:
        result = service.process(payload.dict())

        return {
            "status": "success",
            "engine": "categories",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
