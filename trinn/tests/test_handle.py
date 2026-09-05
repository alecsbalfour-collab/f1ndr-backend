# f1ndr-backend/trinn/tests/test_handle.py
import pytest
from trinn.module import TrinnModule


@pytest.mark.asyncio
async def test_trinn_pipeline_handle():
    module = TrinnModule("mongodb://localhost:27017")
    controller = module.get_controller()
    result = await controller.run_pipeline({"source": "test", "raw": {"id": 1}})
    assert "enrich" in result
    assert "normalize" in result
    assert "transform" in result
