from src.gamestate import GameState
from src.hand import Hand
from src.field import Field, FieldNames
from src.stack import Stack
import enum
import random


class GamePhase(enum.StrEnum):
    CREATE_DECK = "Create deck"
    CURRENT_TURN_MAIN = "Current turn"
    CURRENT_TURN_PLAY_CARD = "Play card on current turn"
    CURRENT_TURN_ATTACK = "Attack enemy on current turn"
    SWAP_PLAYERS = "Swap players"
    GAME_END = "Game end"


class GameServer:
    def __init__(self, state: GameState | None = None, phase: GamePhase | None = None):
        self.game_state = state if state is not None else GameState()
        self.current_phase = phase if phase is not None else GamePhase.CREATE_DECK

    def run(self):
        while self.current_phase != GamePhase.GAME_END:
            self.run_one_step()

    def run_one_step(self):
        phases = {
            GamePhase.CREATE_DECK: create_deck_phase,
            GamePhase.CURRENT_TURN_MAIN: current_turn_main_phase,
            GamePhase.CURRENT_TURN_PLAY_CARD: current_turn_play_card_phase,
            GamePhase.CURRENT_TURN_ATTACK: current_turn_attack_phase,
            GamePhase.SWAP_PLAYERS: swap_players_phase,
            GamePhase.GAME_END: end_game,
        }
        phases[self.current_phase]()

    def create_deck_phase(self):
        self.game_state = GameState()
        self.game_state.attacker.input_interface.choose_cards()
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def current_turn_main_phase(self):
        self.current_phase = (
            self.game_state.attacker.input_interface.choose_current_turn()
        )

    def current_turn_play_card_phase(self):
        self.game_state.attacker.input_interface.try_play_card()

    def current_turn_attack_phase(self):
        self.game_state.attacker.input_interface.unit_attack()

    def swap_players_phase(self):
        self.game_state.attacker.input_interface.turn_end()
        self.current_phase = GamePhase.CURRENT_TURN_MAIN

    def end_game():
        exit(0)
