from pydantic import BaseModel
from typing import Any, Optional

class SuccessResponse(BaseModel):
    status: str = "success"
    message: str
    data: Any

class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
    details: Optional[dict] = None
