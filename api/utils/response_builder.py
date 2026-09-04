from fastapi.responses import JSONResponse

def success_response(data=None, message="OK", status_code=200):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "success",
            "message": message,
            "data": data
        }
    )


def fail_response(message="Error", status_code=400):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "fail",
            "message": message
        }
    )
