from sellr.core.controller_core import SellrController

def test_create_listing():
    c = SellrController()
    result = c.create_listing({"title": "Bike", "price": "100"})
    assert result["status"] == "created"

def test_update_listing():
    c = SellrController()
    result = c.update_listing({"title": "Bike"})
    assert result["status"] == "updated"

def test_remove_listing():
    c = SellrController()
    result = c.remove_listing({"id": "123"})
    assert result["status"] == "removed"
