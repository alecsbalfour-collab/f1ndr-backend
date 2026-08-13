from fastapi import APIRouter, HTTPException
from services.registry.registry_service import RegistryService

router = APIRouter()
service = RegistryService()


@router.get("/registry")
def get_registry():
    """
    Return the full registry using the existing RegistryService.
    """

    try:
        result = service.get_registry()

        return {
            "status": "success",
            "engine": "registry",
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/registry/{item_id}")
def get_registry_item(item_id: str):
    """
    Return a single registry item by ID.
    """

    try:
        result = service.get_item(item_id)

        if not result:
            raise HTTPException(status_code=404, detail="Registry item not found")

        return {
            "status": "success",
            "engine": "registry",
            "item_id": item_id,
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/registry")
def add_registry_item(payload: dict):
    """
    Add a new registry item using the existing RegistryService.
    """

    try:
        result = service.add_item(payload)

        return {
            "status": "success",
            "engine": "registry",
            "input": payload,
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
