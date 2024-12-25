from copy import deepcopy

from src.player import Player
from src.resource import RESOURCE
from src.field import FieldNames


class GameState:
    def __init__(self, p1: Player | None = None, p2: Player | None = None):
        self.attacker = p1 if p1 is not None else Player()
        self.defender = p2 if p2 is not None else Player()

    def attack(self, i_from, i_to):
        """
        card on attacker's side of the field attacks card on defender's side
            i_from - index on the field of the attacker card
            i_to - index on the field of the defending card
        """
        attacker_card = self.attacker.field.get(i_from)
        defender_card = self.defender.field.get(i_to)
        if type(attacker_card) is not Unit or type(defender_card) is not Unit:
            return

        attacker_card.attack(defender_card)
        if not defender_card.is_dead():
            return

        for item in defender_card.items:
            new_card = deepcopy(item)
            self.defender.stack.push(new_card)

        self.defender.field.erase(i_to)
        new_card = deepcopy(DECK[defender_card.id])
        self.defender.stack.push(new_card)

    def play_card(self, i_from, i_to):
        if self.attacker.can_play_card(i_from, i_to):
            self.attacker.play_card(i_from, i_to)

    def swap_players(self):
        self.attacker, self.defender = self.defender, self.attacker

    def turn_end(self):
        self.defender.change_mana(FieldNames.PLAYER, RESOURCE["mana_add_per_turn"])
        self.swap_players()

    def create_gameinfo(self) -> dict:
        # see player_interface -> inform_gameinfo
        pass
