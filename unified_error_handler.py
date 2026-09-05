from logs.logging import error_logger

class ErrorHandler:
    def handle(self, err: Exception) -> dict:
        error_logger.error(str(err))
        return {"status": "error", "message": str(err)}

error_handler = ErrorHandler()
