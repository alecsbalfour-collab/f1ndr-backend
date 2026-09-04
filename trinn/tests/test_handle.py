from trinn import Trinn

def test_handle():
    t = Trinn()
    response = t.handle("Hello Trinn")
    assert "Trinn received" in response
