import enum


class GamePhase(enum.StrEnum):
    CREATE_DECK = "Create deck"
    CURRENT_TURN_MAIN = "Current turn"
    CURRENT_TURN_GAMEINFO = "Get info on current turn"
    CURRENT_TURN_PLAY_CARD = "Play card on current turn"
    CURRENT_TURN_ATTACK = "Attack on current turn"
    CURRENT_TURN_END = "End current turn"
    SWAP_PLAYERS = "Swap players"
    GAME_END = "Game end"
