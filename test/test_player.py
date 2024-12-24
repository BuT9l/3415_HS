import pytest
from src.player import Player
from src.field import Field
from src.hand import Hand
from src.stack import Stack
from src.cards import *


def test_init():
    p = Player(f, h, s)
    assert p.field == f
    assert p.stack == s
    assert p.hand == h


def test_get_card_dmg():
    p = Player(f, h, s)
    dmg = p.get_card_dmg(0)
    assert dmg == 1


def test_get_card_hp():
    p = Player(f, h, s)
    hp = p.get_card_hp(0)
    assert hp == 14


def test_change_card_hp():
    p = Player(f, h, s)
    p.change_card_hp(0, -4)
    assert p.get_card_hp(0) == 10


def test_change_card_dmg():
    p = Player(f, h, s)
    p.change_card_dmg(0, 4)
    assert p.get_card_dmg(0) == 5


def test_can_play_card():
    p = Player(f, h, s)
    assert p.can_play_card(0, 0) == False
    assert p.can_play_card(0, 1) == True

    assert p.can_play_card(2, 0) == False
    assert p.can_play_card(2, 1) == False
    assert p.can_play_card(2, 2) == True

    assert p.can_play_card(2, 4) == False
    assert p.can_play_card(2, 5) == False

    assert p.can_play_card(3, 0) == False
    assert p.can_play_card(3, 1) == False
    assert p.can_play_card(3, 5) == True


def test_play_card():
    p = Player(f, h, s)
    playable_card = p.hand.get_card(0)
    top_card_in_stack = p.stack.get_top_card()
    p.play_card(0, 1)
    assert p.field.get_card(1) == playable_card
    assert p.hand.get_card(0) == top_card_in_stack
