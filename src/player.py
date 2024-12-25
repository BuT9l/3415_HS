from enum import Enum
from typing import Type

from src.cards import Item, Unit, Location, Event
from src.field import Field, FieldNames
from src.hand import Hand
from src.stack import Stack

from src.player_interface import IPlayerInput
from src.players import cli


class Player:
    def __init__(
        self,
        field: Field | None = None,
        hand: Hand | None = None,
        stack: Stack | None = None,
        input_interface: Type[IPlayerInput] = cli.CLI,
    ):
        self.field = field if field is not None else Field()
        self.hand = hand if hand is not None else Hand()
        self.stack = stack if stack is not None else Stack()
        self.input_interface = input_interface

    def can_play_card(self, i_from, i_to):
        card_from = self.hand.get(i_from)
        card_to = self.field.get(i_to)
        card_player = self.field.get(FieldNames.PLAYER)

        if card_from is None:
            return False
        if card_player.mn < card_from.mn:
            return False

        if isinstance(card_from, Location):
            return i_to == FieldNames.LOCATION and card_to is None
        elif isinstance(card_from, Unit):
            return i_to < FieldNames.PLAYER and card_to is None
        elif isinstance(card_from, Item):
            return (
                i_to != FieldNames.LOCATION
                and i_to != FieldNames.PLAYER
                and card_to is not None
            )
        elif isinstance(card_from, Event):
            pass

        return False

    def play_card(self, i_from, i_to):
        card_from = self.hand.pop(i_from)
        card_to = self.field.get(i_to)
        card_player = self.field.get(FieldNames.PLAYER)

        self.hand.push(self.stack.pop(), i_from)

        if isinstance(card_to, Unit):
            card_to.recieve_item(card_from)
        else:
            self.field.place_card(card_from, i_to)

        card_player.mn -= card_from.mn
