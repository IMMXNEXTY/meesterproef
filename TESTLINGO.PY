from woordenlijst import kies_woord, woordenlijst

def test_kies_woord():
    woord = kies_woord()

    assert woord in woordenlijst