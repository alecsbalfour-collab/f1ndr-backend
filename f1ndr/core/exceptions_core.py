"""
f1ndr exceptions.
"""

class F1ndrError(Exception):
    pass


class ScraperError(F1ndrError):
    pass


class EngineError(F1ndrError):
    pass


class ProcessorError(F1ndrError):
    pass


class UnifierError(F1ndrError):
    pass
