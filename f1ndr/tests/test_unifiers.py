from f1ndr.unifiers.listing_unifier import ListingUnifier

def test_unifier_basic():
    unifier = ListingUnifier()
    raw = {"title": "Bike", "price": "100", "url": "/bike"}
    unified = unifier.unify(raw, "kijiji")

    assert unified["title"] == "Bike"
    assert unified["price"] == 100.0
    assert unified["url"] == "/bike"
    assert unified["source"] == "kijiji"
