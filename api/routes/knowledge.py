from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/knowledge")
def knowledge(
    query: Optional[str] = None,
    mode: Optional[str] = "define"
):
    if not query:
        return {"error": "Missing 'query' field"}

    if mode == "define":
        return {
            "action": "define",
            "query": query,
            "output": f"{query}: A general definition placeholder."
        }

    if mode == "facts":
        words = query.split()
        facts = [w for w in words if len(w) > 5]
        return {
            "action": "facts",
            "query": query,
            "output": facts
        }

    if mode == "explain":
        return {
            "action": "explain",
            "query": query,
            "output": f"Explanation placeholder for: {query}"
        }

    return {
        "error": "Invalid mode. Use 'define', 'facts', or 'explain'."
    }
