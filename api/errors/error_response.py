from pydantic import BaseModel
from typing import Any


class ErrorResponse(BaseModel):
    error: str
    message: str
    details: Any | None = None
    request_id: str | None = None
