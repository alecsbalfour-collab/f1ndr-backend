from trinn import Trinn

def test_session():
    t = Trinn()
    t.start_session()
    assert t.session_id in t.db_sessions["active"]

    t.end_session()
    assert t.session_id not in t.db_sessions["active"]
