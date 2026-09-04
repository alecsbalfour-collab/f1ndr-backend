from processors.utils.exception_utils import (
    ProcessorError,
    ProcessorConfigError,
    ProcessorExecutionError,
)


def test_processor_error():
    try:
        raise ProcessorError("test")
    except ProcessorError:
        assert True


def test_processor_config_error():
    try:
        raise ProcessorConfigError("config issue")
    except ProcessorConfigError:
        assert True


def test_processor_execution_error():
    try:
        raise ProcessorExecutionError("execution issue")
    except ProcessorExecutionError:
        assert True
