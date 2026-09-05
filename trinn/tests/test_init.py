# f1ndr-backend/trinn/tests/test_init.py
from trinn import TrinnModule


def test_trinn_init():
    module = TrinnModule("mongodb://localhost:27017")
    assert module.get_controller() is not None
