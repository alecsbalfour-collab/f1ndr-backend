from fastapi import APIRouter, HTTPException
from services.knowledge.knowledge_service import KnowledgeService
from models.knowledge.knowledge_model import build_knowledge_contract

router = APIRouter()
knowledge = KnowledgeService()

@router.post("/add")
def add_fact(payload: dict):
    key = payload.get("key")
    value = payload.get("value")
    category = payload.get("category")

    if not key or not value:
        raise HTTPException(status_code=400, detail="key and value required")

    knowledge.add_fact(key, value, category)
    return {"added": key}

@router.post("/remove")
def remove_fact(payload: dict):
    key = payload.get("key")
    if not key:
        raise HTTPException(status_code=400, detail="key required")

    knowledge.remove_fact(key)
    return {"removed": key}

@router.get("/fact/{key}")
def get_fact(key: str):
    fact = knowledge.get_fact(key)
    if fact is None:
        raise HTTPException(status_code=404, detail="fact not found")
    return {"key": key, "value": fact}

@router.get("/category/{category}")
def get_category(category: str):
    return knowledge.get_category(category)

@router.get("/contract")
def get_contract():
    return build_knowledge_contract(knowledge.snapshot())
