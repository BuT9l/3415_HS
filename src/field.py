from enum import IntEnum
from pathlib import Path

from src.iterable import IterableStaticSize
from src.cards import load_card_from_file, PlayerUnit


class FieldNames(IntEnum):
    UNIT1 = 0
    UNIT2 = 1
    UNIT3 = 2
    UNIT4 = 3
    PLAYER = 4
    LOCATION = 5


class Field(IterableStaticSize):
    def __init__(
        self, cards_list: list | None = None, player_card: PlayerUnit | None = None
    ):
        self.cards_list = (
            cards_list if cards_list is not None else [None] * len(FieldNames)
        )
        self.cards_list[FieldNames.PLAYER] = (
            player_card
            if player_card is not None
            else load_card_from_file(Path("src/standard_player_card.json"))
        )
