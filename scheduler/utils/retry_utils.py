class RetryUtils:
    def execute(self, handler, payload):
        try:
            return handler(payload)
        except Exception as e:
            return {"status": "error", "message": str(e)}


retry_utils = RetryUtils()
