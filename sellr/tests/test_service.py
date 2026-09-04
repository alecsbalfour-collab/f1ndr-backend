from sellr.core.service_core import SellrService

def test_service_create():
    s = SellrService()
    result = s.create_listing({"title": "Item", "price": "10"})
    assert result["output"]["status"] == "active"

def test_service_update():
    s = SellrService()
    result = s.update_listing({"title": "Item"})
    assert result["output"]["title"] == "Item"

def test_service_remove():
    s = SellrService()
    result = s.remove_listing({"id": "1"})
    assert result["output"]["status"] == "removed"
