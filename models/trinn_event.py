# models/trinn_event.py

from pydantic import BaseModel

class TrinnEvent(BaseModel):
    event: str
