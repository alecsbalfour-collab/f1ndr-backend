# models/user_document.py

from pydantic import BaseModel
from typing import Dict, Any

class UserDocument(BaseModel):
    id: str
    email: str
    preferences: Dict[str, Any] = {}
