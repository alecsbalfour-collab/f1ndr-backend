# models/trinn_state.py

from pydantic import BaseModel

class TrinnState(BaseModel):
    state: str
