from enum import IntEnum


class FieldNames(IntEnum):
    UNIT1 = 0
    UNIT2 = 1
    UNIT3 = 2
    UNIT4 = 3
    PLAYER = 4
    LOCATION = 5


class Field:
    def __init__(self, cards_list: list | None = None):
        cards_list = cards_list if cards_list != None else [None] * len(FieldNames)

    def __eq__(self, other):
        for i in range(len(self.cards_list)):
            if self.cards_list[i] != other.cards_list[i]:
                return False
        return True


