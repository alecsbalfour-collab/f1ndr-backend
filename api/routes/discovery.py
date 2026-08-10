from fastapi import APIRouter
from typing import Optional
from discovery.scan import scan
from discovery.classify import classify
from discovery.generator import generate

router = APIRouter()

@router.get("/discover")
def discover(
    mode: Optional[str] = "scan",
    input: Optional[str] = None
):
    if mode == "scan":
        return {
            "action": "scan",
            "input": input,
            "output": scan(input)
        }

    if mode == "classify":
        return {
            "action": "classify",
            "input": input,
            "output": classify(input)
        }

    if mode == "generate":
        return {
            "action": "generate",
            "input": input,
            "output": generate(input)
        }

    return {
        "error": "Invalid mode. Use 'scan', 'classify', or 'generate'."
    }
