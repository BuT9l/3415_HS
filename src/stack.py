class Stack:

    def __init__(self, cards_list=None):
        self.cards_list = cards_list if cards_list != None else []

    def __eq__(self, other):
        for i in range(len(self.cards_list)):

            if self.cards_list[i] != other.cards_list[i]:
                return False
        return True

    def get_top_card(self):
        return self.cards_list[-1]

    def push(self, card):
        self.cards_list.insert(0, card)

    def pop(self):
        if len(self.cards_list) != 0:
            return self.cards_list.pop()
