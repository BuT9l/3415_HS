class IterableStaticSize:
    def __init__(self, length):
        self.cards_list = [None] * length

    def __eq__(self, other):
        for i in range(len(self.cards_list)):
            if self.cards_list[i] != other.cards_list[i]:
                return False
        return True

    def pop(self, index):
        card = self.cards_list[index]
        self.cards_list[index] = None
        return card

    def push(self, card, index):
        self.cards_list[index] = card
        return

    def is_free(self, index):
        return self.cards_list[index] is None
