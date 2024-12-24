from src.field import Field
from src.iterable import IterableStaticSize
from src.resource import RESOURCE


class Hand(IterableStaticSize):
    def __init__(self, cards_list: list | None = None):
        self.cards_list = (
            cards_list if cards_list != None else [None] * RESOURCE.hand_size
        )
