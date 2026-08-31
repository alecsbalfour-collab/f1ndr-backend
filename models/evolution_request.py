# models/evolution_request.py

from pydantic import BaseModel

class EvolutionRequest(BaseModel):
    action: str
    value: int | None = None
