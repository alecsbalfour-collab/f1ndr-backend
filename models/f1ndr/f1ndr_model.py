from pydantic import BaseModel
from typing import Optional

class F1ndrRequest(BaseModel):
    query: Optional[str] = None
