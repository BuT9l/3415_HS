from src.player_interface import IPlayerInput
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.field import FieldNames
    from src.gameserver import GamePhase


class CLI(IPlayerInput):
    def choose_cards(self, all_cards: dict):
        pass

    def choose_current_turn(self): -> "GamePhase":
        while True:
            print("""
    Выберите действие:
1. Посмотреть карты на руке
2. Сыграть карту с руки
3. Атаковать юнита
4. Закончить ход""",
end="\033[4A\033[7C") # Переместить курсор после двоеточия
            choice = input("")
            print("\033[J", end="") # Стереть список действий
            match choice:
                case "1":
                    return GamePhase.CURRENT_TURN_GAMEINFO
                case "2":  # choose_card_to_play()
                    return GamePhase.CURRENT_TURN_PLAY_CARD
                case "3":  # choose_unit_to_attack()
                    return GamePhase.CURRENT_TURN_ATTACK
                case "4":  # turn_end()
                    return GamePhase.CURRENT_TURN_END
                case _:
                    print("Введённое действие не распознано")
        return

    def inform_gameinfo(self, gameinfo: dict):
        pass

    def choose_card_to_play(self, player) -> tuple[int, "FieldNames"]:
        pass

    def choose_unit_to_attack(self, server) -> tuple["FieldNames", "FieldNames"]:
        pass

    def turn_end(self):
        pass
