import random

from src.gamestate import GameState
from src.hand import Hand
from src.stack import Stack
from src.field import FieldNames
from src.gamephases import GamePhase
from src.resource import RESOURCE


class GameServer:
    def __init__(
        self,
        state: GameState | None = None,
        phase: GamePhase | None = None,
        DECK: dict | None = None,
    ):
        self.game_state = state if state is not None else GameState(DECK=DECK)
        self.current_phase = phase if phase is not None else GamePhase.CREATE_DECK

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        phases = {
            GamePhase.CREATE_DECK: self.create_deck_phase,
            GamePhase.CURRENT_TURN_MAIN: self.current_turn_main_phase,
            GamePhase.CURRENT_TURN_GAMEINFO: self.current_turn_gameinfo,
            GamePhase.CURRENT_TURN_PLAY_CARD: self.current_turn_play_card_phase,
            GamePhase.CURRENT_TURN_ATTACK: self.current_turn_attack_phase,
            GamePhase.CURRENT_TURN_END: self.current_turn_end,
            GamePhase.SWAP_PLAYERS: self.swap_players_phase,
            GamePhase.GAME_END: self.end_game,
        }
        phases[self.current_phase]()

    def create_deck_phase(self):
        DECK = self.game_state.DECK
        for player in [self.game_state.attacker, self.game_state.defender]:
            cards = player.input_interface.choose_cards(DECK)
            random.shuffle(cards)
            for card in cards:
                player.stack.push(card)
            for i in range(RESOURCE["hand_size"]):
                player.hand.push(player.stack.pop(), i)
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def current_turn_main_phase(self):
        self.current_phase = (
            self.game_state.attacker.input_interface.choose_current_turn()
        )

    def current_turn_gameinfo(self):
        gameinfo = self.game_state.create_gameinfo()
        self.game_state.attacker.input_interface.inform_gameinfo(gameinfo)
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def current_turn_play_card_phase(self):
        ifrom, ito = self.game_state.attacker.input_interface.choose_card_to_play(
            self.game_state.attacker
        )
        player = self.game_state.attacker
        if player.can_play_card(ifrom, ito):
            player.input_interface.inform_play_card_success()
            self.game_state.attacker.play_card(ifrom, ito)
        else:
            player.input_interface.inform_play_card_failure()
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def current_turn_attack_phase(self):
        ifrom, ito = self.game_state.attacker.input_interface.choose_unit_to_attack()
        if self.game_state.can_attack(ifrom, ito):
            self.game_state.attacker.input_interface.inform_attack_success()
            self.game_state.attack(ifrom, ito)
        else:
            self.game_state.attacker.input_interface.inform_attack_failure()

        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def current_turn_end(self):
        if self.game_state.defender.field.get(FieldNames.PLAYER).is_dead():
            self.current_phase = GamePhase.GAME_END
        elif self.game_state.attacker.field.get(FieldNames.PLAYER).is_dead():
            self.current_phase = GamePhase.GAME_END
        else:
            self.current_phase = GamePhase.SWAP_PLAYERS
        self.game_state.turn_end()

    def swap_players_phase(self):
        self.game_state.swap_players()
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def end_game():
        exit(0)
