from src.player_interface import IPlayerInput
from typing import TYPE_CHECKING
from src.gamephases import GamePhase
from src.field import FieldNames


class CLI(IPlayerInput):
    def choose_cards():
        print("Choose cards not implemented")
        pass

    def choose_current_turn() -> "GamePhase":
        while True:
            print(
                """
    Выберите действие:
1. Посмотреть карты на руке
2. Сыграть карту с руки
3. Атаковать юнита
4. Закончить ход""",
                end="\033[4A\033[7C",
            )  # Переместить курсор после двоеточия
            choice = input()
            print(end="\033[J")  # Стереть список действий
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

    def inform_gameinfo(gameinfo: dict):
        pass

    def choose_card_to_play(player) -> tuple[int, "FieldNames"]:
        pass

    def choose_unit_to_attack(server) -> tuple["FieldNames", "FieldNames"]:
        pass

    def turn_end():
        pass
