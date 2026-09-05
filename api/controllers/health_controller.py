from utils.response_builder import success_response

class HealthController:
    """
    Basic health check controller.
    """

    def get_status(self):
        return success_response({"status": "healthy"}, "Service is running")


health_controller = HealthController()
