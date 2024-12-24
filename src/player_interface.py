from abc import ABC, abstractmethod

# from src.gameserver import GamePhase circular import
from src.field import FieldNames


class IPlayerInput(ABC):
    # CREATE_DECK
    @abstractmethod
    def choose_cards(self, all_cards: dict):
        """
        Просит игрока выбрать 8 карт из всех доступных карт
        """
        pass

    # CURRENT_TURN_MAIN
    @abstractmethod
    def choose_current_turn(self):# -> GamePhase: circular import
        """
        Выбрать, какое действие вы хотите сделать за ход. (Какая фаза будет следующей)
        Можно:
            Вывести информацию об игре
            попробовать сыграть карту,
            атаковать юнитом,
            закончить ход.
        """
        pass

    # CURRENT_TURN_PLAY_CARD
    @abstractmethod
    def choose_card_to_play(self, player) -> tuple[int, FieldNames]:
        """
        Выбрать, какую карту вы хотите сыграть и проверить возможность такой игры
        Возвращает 2 значения:
            ifrom - какую карту играем с руки
            ito - куда играем карту на поле
        """
        pass

    # CURRENT_TURN_ATTACK
    @abstractmethod
    def choose_unit_to_attack(self, server) -> tuple[FieldNames, FieldNames]:
        """
        Атакуем юнитом вражеского юнита и проверяем возможность атаки
        Возвращает 2 значения:
            ifrom / attacker - кто атакует
            ito / defender - кого атакуем
        """
        pass

    @abstractmethod
    def turn_end(self):
        """
        Закончить свой ход
        """
        pass
