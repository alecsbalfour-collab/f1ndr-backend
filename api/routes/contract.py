from fastapi import APIRouter, HTTPException
from services.contract.contract_service import ContractService
from models.contract.contract_model import ContractRequest

router = APIRouter()
service = ContractService()

@router.post("/contract")
def contract(payload: ContractRequest):
    try:
        result = service.process(payload.dict())

        return {
            "status": "success",
            "engine": "contract",
            "input": payload.dict(),
            "output": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
