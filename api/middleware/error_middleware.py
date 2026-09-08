async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content=error_response(
                message="Internal server error",
                details=str(exc)
            )
        )
