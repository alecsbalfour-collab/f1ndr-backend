# models/voice_request.py

from pydantic import BaseModel

class VoiceRequest(BaseModel):
    query: str
