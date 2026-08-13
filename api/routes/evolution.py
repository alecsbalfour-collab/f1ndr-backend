from fastapi import APIRouter, HTTPException
from services.evolution.evolution_service import EvolutionService
from models.evolution.evolution_model import EvolutionRequest

router = APIRouter()
service = EvolutionService()


@router.post("/evolution")
def run_evolution(payload: EvolutionRequest):
    """
    Run an evolution cycle using the existing EvolutionService.
    This wires the route → service → engine → model exactly as your architecture intends.
    """

    try:
        result = service.evolve(payload)

        return {
            "status": "success",
            "engine": "evolution",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
