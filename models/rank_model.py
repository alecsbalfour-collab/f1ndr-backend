from pydantic import BaseModel

class RankMetadata(BaseModel):
    score: float
    reason: str
