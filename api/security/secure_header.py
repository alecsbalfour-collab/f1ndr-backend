from fastapi import FastAPI


def add_secure_headers(app: FastAPI):
    @app.middleware("http")
    async def secure_headers(request, call_next):
        response = await call_next(request)

        # Security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"

        return response
