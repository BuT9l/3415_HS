from src.player_interface import IPlayerInput
from src.field import FieldNames


class CLI(IPlayerInput):
    def choose_cards(self, all_cards: dict):
        pass

    def choose_current_turn(self):  # -> GamePhase:
        match int(
            input(
                """
                        Действие:
                    1. Посмотреть карты на руке
                    2. Сыграть карту с руки
                    3. Атаковать юнита
                    4. Закончить ход
                    """
            )
        ):
            case 1:
                pass
            case 2:  # choose_card_to_play()
                pass
            case 3:  # choose_unit_to_attack()
                pass
            case 4:  # turn_end()
                pass
        return

    def choose_card_to_play(self, player) -> tuple[int, FieldNames]:
        pass

    def choose_unit_to_attack(self, server) -> tuple[FieldNames, FieldNames]:
        pass

    def turn_end(self):
        pass
