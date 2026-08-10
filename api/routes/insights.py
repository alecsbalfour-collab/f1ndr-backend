from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/insights")
def insights(
    text: Optional[str] = None,
    mode: Optional[str] = "summary"
):
    if not text:
        return {"error": "Missing 'text' field"}

    if mode == "summary":
        return {
            "action": "summary",
            "input": text,
            "output": f"Summary: {text[:75]}..."
        }

    if mode == "keywords":
        words = text.split()
        keywords = list({w.lower().strip(",.!?") for w in words if len(w) > 4})
        return {
            "action": "keywords",
            "input": text,
            "output": keywords
        }

    if mode == "sentiment":
        sentiment = "neutral"
        lowered = text.lower()
        if any(w in lowered for w in ["love", "great", "awesome", "perfect"]):
            sentiment = "positive"
        if any(w in lowered for w in ["hate", "terrible", "bad", "awful"]):
            sentiment = "negative"

        return {
            "action": "sentiment",
            "input": text,
            "output": sentiment
        }

    return {
        "error": "Invalid mode. Use 'summary', 'keywords', or 'sentiment'."
    }
