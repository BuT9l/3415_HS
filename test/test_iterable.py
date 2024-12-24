import pytest
from src.field import Field
from src.hand import Hand
from src.iterable import IterableStaticSize
from src.cards import *

DECK = load_cards(Path("cards/"))


def test_prereq():
    assert DECK is not None


def test_init():
    a = IterableStaticSize(length=5)
    b = IterableStaticSize(cards_list=[1, 2, 3, 4, 5])
    assert len(a.cards_list) == 5
    assert len(b.cards_list) == 5
    assert b.cards_list[2] == 3


def test_init_field():
    a = Field(["a", "b", "c", "d", "e", "f"])
    b = Field()
    assert len(b.cards_list) == 6
    assert a.get(0) == "a"
    assert a.get(3) == "d"
    assert b.get(4) == None


def test_init_hand():
    a = Hand(["x", "d", "s", "e"])
    b = Hand()
    assert len(b.cards_list) == 4
    assert a.get(0) == "x"
    assert a.get(2) == "s"
    assert b.get(1) == None


def test_get():
    a = IterableStaticSize(cards_list=[1, 2])
    assert a.get(0) == a.cards_list[0]
    assert a.get(1) == a.cards_list[1]


def test_erase():
    a = IterableStaticSize(cards_list=[1, 2, 3, 4])
    a.erase(1)
    a.erase(3)
    assert a.get(1) is None
    assert a.get(3) is None
    assert a.get(0) is not None
    assert a.get(2) is not None


def test_pop():
    a = IterableStaticSize(cards_list=[1, 2, 3, 4])
    a2 = a.pop(2)
    a0 = a.pop(0)
    assert a2 is not None
    assert a0 is not None
    assert a.get(1) is not None
    assert a.get(3) is not None
    assert a.get(0) is None
    assert a.get(2) is None


def test_push():
    a = IterableStaticSize(length=5)
    a.push("karta", 3)
    assert a.get(3) == "karta"
    assert a.get(2) is None
    assert a.get(4) is None


def test_is_free():
    a = IterableStaticSize(cards_list=["abcd", None])
    assert a.is_free(0) is False
    assert a.is_free(1) is True
