# models/search_request.py

from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
