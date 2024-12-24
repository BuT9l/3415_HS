import pytest


def test_load_cards():
    DECK = load_cards(Path("cards/"))
    assert DECK is not None
