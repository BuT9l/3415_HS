import pytest
from pathlib import Path
from src.cards import (
    Card,
    Item,
    Unit,
    PlayerUnit,
    Location,
    Event,
    load_card_from_file,
    load_cards,
)


def test_load_cards():
    DECK = load_cards(Path("cards/"))
    assert DECK is not None
