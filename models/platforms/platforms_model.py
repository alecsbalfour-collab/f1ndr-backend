from pydantic import BaseModel
from typing import Optional

class PlatformsRequest(BaseModel):
    category: Optional[str] = None
