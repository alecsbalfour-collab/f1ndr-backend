from fastapi import APIRouter, HTTPException
from services.trinn.trinn_service import TrinnService
from models.trinn.trinn import TrinnRequest

router = APIRouter()
service = TrinnService()


@router.post("/trinn")
def trinn_core(payload: TrinnRequest):
    """
    Core Trinn endpoint.
    Handles character creation, updates, inference, and execution
    using the existing TrinnService.
    """

    try:
        result = service.process(payload)

        return {
            "status": "success",
            "engine": "trinn",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/trinn/update")
def trinn_update(payload: dict):
    """
    Update a Trinn character's state, memory, or attributes.
    """

    try:
        result = service.update(payload)

        return {
            "status": "success",
            "engine": "trinn_update",
            "input": payload,
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router