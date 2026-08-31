# models/trinn_contract.py

from pydantic import BaseModel
from typing import Any, Dict


class TrinnContract(BaseModel):
    state: Dict[str, Any]
    memory: Dict[str, Any]
    personality: Dict[str, Any]
    emotion: str
    reinforcement: str
    animation: Dict[str, Any]


def build_trinn_contract(
    state_snapshot,
    memory_snapshot,
    personality_snapshot,
    emotion,
    reinforcement,
    animation_snapshot
):
    return TrinnContract(
        state=state_snapshot,
        memory=memory_snapshot,
        personality=personality_snapshot,
        emotion=emotion,
        reinforcement=reinforcement,
        animation=animation_snapshot
    )
