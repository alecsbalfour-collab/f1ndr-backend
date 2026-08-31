# models/trinn_memory_document.py

from pydantic import BaseModel
from typing import Dict, Any

class TrinnMemoryDocument(BaseModel):
    id: str
    memory: Dict[str, Any]
