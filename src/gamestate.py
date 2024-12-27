from copy import deepcopy

from src.player import Player
from src.resource import RESOURCE
from src.field import FieldNames
from src.cards import Unit


class GameState:
    def __init__(
        self,
        p1: Player | None = None,
        p2: Player | None = None,
        DECK: dict | None = None,
    ):
        self.attacker = p1 if p1 is not None else Player()
        self.defender = p2 if p2 is not None else Player()
        if DECK is not None:
            self.DECK = DECK
        else:
            raise Exception("You need cards to play game")
        self.attacked_list = list()

    def can_attack(self, i_from, i_to):
        attacker_card = self.attacker.field.get(i_from)
        defender_card = self.defender.field.get(i_to)
        if (
            isinstance(attacker_card, Unit)
            and isinstance(defender_card, Unit)
            and i_from not in self.attacked_list
        ):
            return True
        return False

    def attack(self, i_from, i_to):
        """
        card on attacker's side of the field attacks card on defender's side
            i_from - index on the field of the attacker card
            i_to - index on the field of the defending card
        """
        attacker_card = self.attacker.field.get(i_from)
        defender_card = self.defender.field.get(i_to)

        attacker_card.attack(defender_card)
        self.attacked_list.append(i_from)
        if not defender_card.is_dead():
            return

        for item in defender_card.items:
            new_card = deepcopy(self.DECK[item.id])
            self.defender.stack.push(new_card)

        self.defender.field.erase(i_to)
        new_card = deepcopy(self.DECK[defender_card.id])
        self.defender.stack.push(new_card)

    def swap_players(self):
        self.attacker, self.defender = self.defender, self.attacker

    def turn_end(self):
        player_card = self.defender.field.get(FieldNames.PLAYER)
        self.attacked_list = list()
        player_card.mn += RESOURCE["mana_add_per_turn"]

    def create_gameinfo(self) -> dict:
        # see player_interface -> inform_gameinfo
        gameinfo = dict()
        gameinfo["my_field"] = deepcopy(self.attacker.field.cards_list)
        gameinfo["enemy_field"] = deepcopy(self.defender.field.cards_list)
        gameinfo["my_hand"] = deepcopy(self.attacker.hand.cards_list)
        # gameinfo["events"] = ???
        return gameinfo
