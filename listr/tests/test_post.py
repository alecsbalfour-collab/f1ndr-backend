from listr.listr import LisTr
from utils.exceptions import ServiceError

listr = LisTr()

def test_post_success():
    item = {
        "id": "123",
        "title": "Test Title",
        "description": "Test Description"
    }
    result = listr.post(item)
    assert result["id"] == "123"

def test_post_missing_id():
    item = {
        "title": "Test Title",
        "description": "Test Description"
    }
    try:
        listr.post(item)
        assert False
    except ServiceError:
        assert True

def test_post_batch():
    items = [
        {"id": "1", "title": "A", "description": "B"},
        {"id": "2", "title": "C", "description": "D"},
    ]
    results = listr.post_batch(items)
    assert len(results) == 2
