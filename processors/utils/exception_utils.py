class ProcessorError(Exception):
    """
    Enterprise-level base exception for processor-related errors.
    """
    pass


class ProcessorConfigError(ProcessorError):
    """
    Raised when processor configuration is invalid.
    """
    pass


class ProcessorExecutionError(ProcessorError):
    """
    Raised when processor execution fails.
    """
    pass
