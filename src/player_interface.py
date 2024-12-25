from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from src.field import FieldNames
    from src.gameserver import GamePhase


class IPlayerInput(ABC):
    # CREATE_DECK
    @staticmethod
    @abstractmethod
    def choose_cards(self, all_cards: dict):
        """
        Просит игрока выбрать 8 карт из всех доступных карт
        """
        pass

    # CURRENT_TURN_MAIN
    @staticmethod
    @abstractmethod
    def choose_current_turn(self) -> "GamePhase":
        """
        Выбрать, какое действие вы хотите сделать за ход. (Какая фаза будет следующей)
        Можно:
            Вывести информацию об игре
            попробовать сыграть карту,
            атаковать юнитом,
            закончить ход.
        """
        pass

    @staticmethod
    def inform_gameinfo(self, info):
        """
        Получает информацию о состоянии игры в виде словаря:
            Состояние своего поля (my_field) и поля врага(enemy_field) - Списки из 6 элементов:
                Информация о каждом юните
                    Информация о вещах соодтветствующего юнита(items)
                Информация о локации 5 поле в списке
                Текущие ивенты (TODO)
            Информация о каждой карте на руке(my_hand) - список из RESOURCE["hand_size"] элементов
        """

    # CURRENT_TURN_PLAY_CARD
    @staticmethod
    @abstractmethod
    def choose_card_to_play(self, player) -> tuple[int, "FieldNames"]:
        """
        Выбрать, какую карту вы хотите сыграть и проверить возможность такой игры
        Возвращает 2 значения:
            ifrom - какую карту играем с руки
            ito - куда играем карту на поле
        """
        pass

    # CURRENT_TURN_ATTACK
    @staticmethod
    @abstractmethod
    def choose_unit_to_attack(self, server) -> tuple["FieldNames", "FieldNames"]:
        """
        Атакуем юнитом вражеского юнита и проверяем возможность атаки
        Возвращает 2 значения:
            ifrom / attacker - кто атакует
            ito / defender - кого атакуем
        """
        pass

    @staticmethod
    @abstractmethod
    def turn_end(self):
        """
        Закончить свой ход
        """
        pass
