from fastapi import APIRouter, HTTPException
from services.dialogue.dialogue_service import DialogueService
from models.dialogue.dialogue_model import DialogueRequest

router = APIRouter()
service = DialogueService()


@router.post("/dialogue")
def generate_dialogue(payload: DialogueRequest):
    """
    Generate dialogue using the existing DialogueService.
    This wires the route → service → engine → model exactly as your architecture intends.
    """

    try:
        result = service.generate_dialogue(payload)

        return {
            "status": "success",
            "engine": "dialogue",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
