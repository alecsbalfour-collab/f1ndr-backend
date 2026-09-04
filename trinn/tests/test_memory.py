from trinn import Trinn

def test_memory():
    t = Trinn()
    t.remember("city", "Calgary")
    assert t.recall("city") == "Calgary"
