from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    query: str
    results: list[dict]
