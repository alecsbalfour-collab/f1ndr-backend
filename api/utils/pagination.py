from typing import Any, Dict, List

def paginate(items: List[Any], page: int = 1, size: int = 20) -> Dict[str, Any]:
    """
    Simple pagination utility.
    """
    start = (page - 1) * size
    end = start + size

    return {
        "page": page,
        "size": size,
        "total": len(items),
        "results": items[start:end],
    }
