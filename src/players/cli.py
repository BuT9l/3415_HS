from copy import deepcopy

from src.player_interface import IPlayerInput
from src.gamephases import GamePhase
from src.field import Field, FieldNames
from src.cards import Card, Unit, PlayerUnit, Item, Location, Event
from src.resource import RESOURCE


class CLI(IPlayerInput):
    def __init__(self):
        pass

    def choose_cards(self, DECK: dict) -> list[8]:
        while True:
            print("Доступные карты для выбора:")
            i = 1
            callback = dict()
            for key in DECK:
                print(f"{i}. {DECK[key].name}")
                callback[str(i)] = key
                i += 1
            choice = input(
                "Выберите карты, с которыми вы будете играть (номера карт через пробел):"
            )
            chosen_cards = list()
            for key in callback:
                if key in choice:
                    chosen_cards.append(deepcopy(DECK[callback[key]]))
            if len(chosen_cards) != 8:
                print("Вы должны выбрать 8 карт")
                continue
            return chosen_cards

    def choose_current_turn(self) -> GamePhase:
        print(
            """
1. Посмотреть всю информацию об игре
2. Сыграть карту с руки
3. Атаковать юнита
4. Закончить ход"""
        )
        while True:
            print("Выберите действие:", end=" ")
            choice = input()
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

    def repr_player(self, card: PlayerUnit, indent=1):
        s = str()
        s += "\t" * indent
        s += f"[Игрок] {card.name}"
        s += "\n" + "\t" * indent
        s += f"\tМана: {card.mn}"
        s += "\n" + "\t" * indent
        s += f"\tЗдоровье: {card.hp}"
        return s

    def repr_location(self, card: Location, indent=1):
        s = str()
        s += "\t" * indent
        s += f"[Локация] [{card.fract}] {card.name}"
        s += "\n" + "\t" * indent
        s += f"\tСтоимость: {card.mn}"
        s += "\n" + "\t" * indent
        s += f"\tУрон: +{card.dmg_boost}"
        s += "\n" + "\t" * indent
        s += f"\tЗдоровье: +{card.hp_boost}"
        return s

    def repr_item(self, card: Item, indent=1):
        s = str()
        s += "\t" * indent
        s += f"[Предмет] [{card.fract}] {card.name}"
        s += "\n" + "\t" * indent
        s += f"\tСтоимость: {card.mn}"
        s += "\n" + "\t" * indent
        s += f"\tУрон: +{card.dmg_boost}"
        s += "\n" + "\t" * indent
        s += f"\tЗдоровье: +{card.hp_boost}"
        return s

    def repr_unit(self, card: Unit, indent=1):
        s = str()
        s += "\t" * indent
        s += f"[Юнит] [{card.fract}] {card.name}"
        s += "\n" + "\t" * indent
        s += f"\tСтоимость: {card.mn}"
        s += "\n" + "\t" * indent
        s += f"\tЗдоровье: {card.hp}"
        s += "\n" + "\t" * indent
        s += f"\tУрон: {card.dmg}"
        if len(card.items) != 0:
            s += "\n" + "\t" * indent
            s += f"\tШмотки:"
            for shmotka in card.items:
                s += "\n"
                s += repr_item(shmotka, indent=2)
        return s

    def repr_event(self, card: Event, indent=1):
        s = str()
        s += "\t" * indent
        s += f"[Ивент] [{card.fract}] {card.name}"
        s += "\n" + "\t" * indent
        s += f"\tСтоимость: {card.mn}"
        return s

    def inform_gameinfo_field_printer(self, field: list):
        i = 1
        for item in field:
            print(f"{i}:", end="")
            i += 1
            if item is None:
                print("\t[Пустой слот]")
            elif isinstance(item, PlayerUnit):
                print(self.repr_player(item))
            elif isinstance(item, Location):
                print(self.repr_location(item))
            elif isinstance(item, Unit):
                print(self.repr_unit(item))

    def inform_gameinfo_hand_printer(self, hand: list):
        i = 1
        for item in hand:
            print(f"{i}:", end="")
            i += 1
            if item is None:
                print("\t[Пустой слот]")
            elif isinstance(item, Unit):
                print(self.repr_unit(item))
            elif isinstance(item, Item):
                print(self.repr_item(item))
            elif isinstance(item, Location):
                print(self.repr_location(item))
            elif isinstance(item, Event):
                print(self.repr_event(item))

    def inform_gameinfo(self, gameinfo: dict):
        print("Вражеское поле:")
        self.inform_gameinfo_field_printer(gameinfo["enemy_field"])
        print("Ваше поле:")
        self.inform_gameinfo_field_printer(gameinfo["my_field"])
        print("Карты на руке:")
        self.inform_gameinfo_hand_printer(gameinfo["my_hand"])

    def choose_card_to_play(self, player) -> tuple[int, FieldNames]:
        while True:
            print("Выберите номер карты, которую вы хотите сыграть:", end=" ")
            try:
                ifrom = int(input())
                if ifrom < 1 or ifrom > RESOURCE["hand_size"]:
                    print("Такого индекса нету")
                    continue
            except ValueError:
                print("Напечатайте число")
                continue
            break

        while True:
            print("Выберите номер поля, куда вы хотите сыграть карту:", end=" ")
            try:
                ito = int(input())
                if ito < 1 or ito > len(FieldNames):
                    print("Такого индекса нету")
                    continue
            except ValueError:
                print("Напечатайте число")
                continue
            break
        return (ifrom - 1, ito - 1)

    def inform_play_card_success(self):
        print("Карта разыграна")

    def inform_play_card_failure(self):
        print("Вы не можете разыграть карту так")

    def choose_unit_to_attack(self) -> tuple[FieldNames, FieldNames]:
        while True:
            print("Выберите номер юнита, которым вы хотите атаковать", end=" ")
            try:
                ifrom = int(input())
                if ifrom < 1 or ifrom > len(FieldNames):
                    print("Такого индекса нету")
                    continue
                if ifrom + 1 == FieldNames.PLAYER:
                    print("Вы не можете атаковать игроком")
                    continue
                if ifrom + 1 == FieldNames.LOCATION:
                    print("Это локация, она не обладает умением атаковать")
                    continue
            except ValueError:
                print("Напечатайте число")
                continue
            break

        while True:
            print(
                "Выберите номер вражеского юнита, которого вы хотите атаковать:",
                end=" ",
            )
            try:
                ito = int(input())
                if ito < 1 or ito > len(FieldNames):
                    print("Такого индекса нету")
                    continue
                if ifrom + 1 == FieldNames.LOCATION:
                    print("Это локация, вы не можете её атаковать")
                    continue
            except ValueError:
                print("Напечатайте число")
                continue
            break
        return (ifrom - 1, ito - 1)

    def inform_attack_success(self):
        print("Юнит атакует!!")

    def inform_attack_failure(self):
        print("Вы не можете так атаковать")
