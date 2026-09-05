class CoreHelpers:
    def normalize(self, value):
        return value.strip().lower() if isinstance(value, str) else value

core_helpers = CoreHelpers()
