from fastapi import APIRouter, HTTPException
from services.registry_service import RegistryService
from services.trinn_controller import TrinnController

router = APIRouter()
registry = RegistryService()

@router.get("/characters")
def list_characters():
    return registry.list_characters()

@router.post("/characters/{name}")
def add_character(name: str):
    if registry.get_character(name):
        raise HTTPException(status_code=400, detail="Character already exists")

    registry.add_character(name, TrinnController())
    return {"added": name}

@router.delete("/characters/{name}")
def remove_character(name: str):
    if not registry.get_character(name):
        raise HTTPException(status_code=404, detail="Character not found")

    registry.remove_character(name)
    return {"removed": name}

@router.get("/characters/{name}/contract")
def get_character_contract(name: str):
    char = registry.get_character(name)
    if not char:
        raise HTTPException(status_code=404, detail="Character not found")

    # requires emotion + reinforcement from interaction engine
    return char.get_contract({}, {})
