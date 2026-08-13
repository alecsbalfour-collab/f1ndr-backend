from pydantic import BaseModel
from typing import Optional, Dict, Any

class ContractRequest(BaseModel):
    contract_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None
