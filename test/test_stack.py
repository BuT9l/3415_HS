import pytest
from src.stack import Stack


def test_init():
    s = Stack([1, 2, 3, 4, 5, 6])
    assert s.cards_list[0] == 1
    assert s.cards_list[4] == 5


def test_push():
    s = Stack([5, 4, 3, 2, 1])
    s.push(6)
    s.push(7)
    assert s.cards_list[0] == 7
    assert s.cards_list[1] == 6
    assert s.cards_list[2] == 5


def test_pop():
    s = Stack([7, 6, 5, 4, 3, 2, 1])
    s.push(s.pop())
    s.push(s.pop())
    assert s.cards_list[0] == 2
    assert s.cards_list[1] == 1
    assert s.cards_list[2] == 7
    assert s.cards_list[3] == 6
