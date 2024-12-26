from src.gamestate import GameState
from src.hand import Hand
from src.stack import Stack
from src.gamephases import GamePhase
import random


class GameServer:
    def __init__(self, state: GameState | None = None, phase: GamePhase | None = None):
        self.game_state = state if state is not None else GameState()
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
        self.game_state.attacker.input_interface.choose_cards()
        self.game_state.defender.input_interface.choose_cards()
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def current_turn_main_phase(self):
        self.current_phase = (
            self.game_state.attacker.input_interface.choose_current_turn()
        )

    def current_turn_gameinfo(self):
        gameinfo = self.game_state.create_gameinfo()
        self.game_state.attacker.input_interface.inform_gameinfo(gameinfo)
        self.current_phase = GamePhase.CURRENT_TURN_MAIN
        pass

    def current_turn_end(self):
        pass

    def current_turn_play_card_phase(self):
        self.game_state.attacker.input_interface.try_play_card()

    def current_turn_attack_phase(self):
        self.game_state.attacker.input_interface.unit_attack()

    def swap_players_phase(self):
        self.game_state.attacker.input_interface.turn_end()
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def end_game():
        exit(0)
