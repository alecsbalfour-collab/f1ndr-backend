from pydantic import BaseModel

class ListingCreate(BaseModel):
    title: str
    description: str
    price: float
    photos: list[str] | None = None
    category: str | None = None
    condition: str | None = None
    location: str | None = None
    tags: list[str] | None = None
