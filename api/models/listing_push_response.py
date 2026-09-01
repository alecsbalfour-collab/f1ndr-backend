from pydantic import BaseModel

class ListingPushResponse(BaseModel):
    status: str
    platforms: list[str]
