class Stack:

    def __init__(self, cards_list: list | None = None):
        self.cards_list = cards_list if cards_list is not None else list()

    def push(self, card):
        self.cards_list.insert(0, card)

    def pop(self):
        if len(self.cards_list) != 0:
            return self.cards_list.pop()
