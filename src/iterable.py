class IterableStaticSize:
    def __init__(self, length: int | None = None, cards_list: list | None = None):
        self.cards_list = cards_list if cards_list is not None else [None] * length

    def get(self, index):
        return self.cards_list[index]

    def erase(self, index):
        self.cards_list[index] = None

    def pop(self, index):
        card = self.cards_list[index]
        self.cards_list[index] = None
        return card

    def push(self, card, index):
        self.cards_list[index] = card
        return

    def is_free(self, index):
        return self.cards_list[index] is None
