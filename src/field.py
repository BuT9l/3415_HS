from enum import IntEnum
from src.iterable import IterableStaticSize


class FieldNames(IntEnum):
    UNIT1 = 0
    UNIT2 = 1
    UNIT3 = 2
    UNIT4 = 3
    PLAYER = 4
    LOCATION = 5


class Field(IterableStaticSize):
    def __init__(self, cards_list: list | None = None):
        self.cards_list = (
            cards_list if cards_list is not None else [None] * len(FieldNames)
        )
