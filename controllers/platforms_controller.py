from services.f1ndr.platforms_service import PlatformsService

class PlatformsController:
    """
    Controller for platform metadata and validation.
    """

    def __init__(self):
        self.service = PlatformsService()

    def supported(self):
        return self.service.get_supported()

    def validate(self, platforms):
        return self.service.validate(platforms)
