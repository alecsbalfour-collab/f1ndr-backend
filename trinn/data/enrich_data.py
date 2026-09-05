# f1ndr-backend/trinn/data/enrich_data.py
"""
TRINN enrich data utilities.
"""

def build_enrich_payload(raw: dict) -> dict:
    return {
        "source": raw.get("source"),
        "raw": raw,
        "metadata": raw.get("metadata", {}),
    }
