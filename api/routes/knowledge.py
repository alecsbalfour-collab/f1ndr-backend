from fastapi import APIRouter, HTTPException
from services.knowledge.knowledge_service import KnowledgeService
from models.knowledge.knowledge_model import KnowledgeRequest

router = APIRouter()
service = KnowledgeService()


@router.post("/knowledge")
def generate_knowledge(payload: KnowledgeRequest):
    """
    Generate knowledge inference using the existing KnowledgeService.
    This wires the route → service → engine → model exactly as your architecture intends.
    """

    try:
        result = service.generate_knowledge(payload)

        return {
            "status": "success",
            "engine": "knowledge",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
