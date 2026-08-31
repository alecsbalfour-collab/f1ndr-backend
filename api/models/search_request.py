from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    platforms: list[str] | None = None
