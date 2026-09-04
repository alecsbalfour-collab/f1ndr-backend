from listr.core.controller_core import LisTrController

def test_post():
    c = LisTrController()
    result = c.post({"title": "Test"})
    assert result["status"] == "posted"

def test_validate():
    c = LisTrController()
    result = c.validate({"title": "Test", "price": "10", "location": "Calgary"})
    assert result["status"] == "validated"
