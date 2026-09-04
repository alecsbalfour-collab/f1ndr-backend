class APIError(Exception):
    def __init__(self, message: str, status_code: int = 400, details: dict | None = None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class NotFoundError(APIError):
    def __init__(self, message="Resource not found", details=None):
        super().__init__(message, 404, details)


class ValidationError(APIError):
    def __init__(self, message="Validation failed", details=None):
        super().__init__(message, 422, details)


class UnauthorizedError(APIError):
    def __init__(self, message="Unauthorized", details=None):
        super().__init__(message, 401, details)
