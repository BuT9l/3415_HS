from abc import ABC, abstractmethod
from src.gamephases import GamePhase
from src.field import Field, FieldNames


class IPlayerInput(ABC):
    # CREATE_DECK
    @abstractmethod
    def choose_cards(self):
        """
        Просит игрока выбрать 8 карт из всех доступных карт
        Ожидается что присутствует глобальная переменная DECK со всеми используемыми картами
        """
        pass

    # CURRENT_TURN_MAIN
    @abstractmethod
    def choose_current_turn(self) -> GamePhase:
        """
        Выбрать, какое действие вы хотите сделать за ход. (self,Какая фаза будет следующей)
        Можно:
            Вывести информацию об игре
            попробовать сыграть карту,
            атаковать юнитом,
            закончить ход.
        """
        pass

    def inform_gameinfo(self, gameinfo: dict):
        """
        Получает информацию о состоянии игры в виде словаря:
            Состояние своего поля (my_field) и поля врага(enemy_field) - Списки из 6 элементов:
                Информация о каждом юните
                    Информация о вещах соодтветствующего юнита(items)
                Информация о локации 5 поле в списке
                Текущие ивенты (TODO)
            Информация о каждой карте на руке(my_hand) - список размером RESOURCE["hand_size"] элементов
        """

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
    def choose_unit_to_attack(self, field: Field) -> tuple[FieldNames, FieldNames]:
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
