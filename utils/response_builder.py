from fastapi.responses import JSONResponse
from datetime import datetime, timezone

def success_response(data=None, message="Operation successful", status_code=200):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": data,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )

def error_response(message="An error occurred", status_code=400, details=None):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "details": details,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )
