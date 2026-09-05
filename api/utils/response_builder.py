from typing import Any, Dict

def success_response(data: Any, message: str = "OK") -> Dict[str, Any]:
    """
    Unified success response builder.
    """
    return {
        "status": "success",
        "message": message,
        "data": data,
    }


def created_response(data: Any, message: str = "Created") -> Dict[str, Any]:
    """
    Unified creation response builder.
    """
    return {
        "status": "created",
        "message": message,
        "data": data,
    }
