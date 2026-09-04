from trinn import Trinn

def test_init():
    t = Trinn()
    assert t.session_id is not None
    assert isinstance(t.settings, dict)
