from pydantic import BaseModel

class ListingCreateResponse(BaseModel):
    status: str
    listing_id: str | None = None
