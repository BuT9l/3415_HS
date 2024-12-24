import json
from pathlib import Path
from os import listdir
from os.path import isfile


class Card:

    def __init__(self, id, name, fract, mn):
        self.id = id
        self.name = name
        self.fract = fract
        self.mn = mn

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.fract == other.fract
            and self.mn == other.mn
        )

    @classmethod
    def load(cls, file):
        return cls(id=file["id"], name=file["name"], fract=file["fract"], mn=file["mn"])


class Item(Card):

    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

    def __eq__(self, other):
        return (
            Card.__eq__(self, other)
            and self.dmg_boost == other.dmg_boost
            and self.hp_boost == other.hp_boost
        )

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg_boost=file["dmg_boost"],
            hp_boost=file["hp_boost"],
        )


class Unit(Card):

    def __init__(self, id, name, fract, mn, dmg, hp, items):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg = dmg
        self.hp = hp
        self.items = items if items is not None else list()

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg=file["dmg"],
            hp=file["hp"],
            items=file.get(
                "items"
            ),  # get() will return None if items does not exist, and they does not in plain cards from repo
        )

    def can_recieve_item(self, item):
        return item.fract == self.fract

    def recieve_item(self, item: Item):
        self.items.append(item)
        self.hp += item.hp_boost
        self.dmg += item.dmg_boost

    def attack(self, other):
        other.hp -= self.dmg

    def is_dead(self):
        return self.hp < 0


class Location(Card):
    def __init__(self, id, name, fract, mn, dmg_boost, hp_boost):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg_boost = dmg_boost
        self.hp_boost = hp_boost

    def __eq__(self, other):
        return (
            Card.__eq__(self, other)
            and self.dmg_boost == other.dmg_boost
            and self.hp_boost == other.hp_boost
        )

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg_boost=file["dmg_boost"],
            hp_boost=file["hp_boost"],
        )


class Event(Card):
    def __init__(self, id, name, fract, mn):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)

    @classmethod
    def load(cls, file):
        return cls(id=file["id"], name=file["name"], fract=file["fract"], mn=file["mn"])


class PlayerUnit(Unit):
    def __init__(self, id, name, fract, mn, dmg, hp, items):
        super().__init__(
            id=id, name=name, fract=fract, mn=mn, dmg=dmg, hp=hp, items=items
        )

    @classmethod
    def load(cls, file):
        return cls(
            id=file["id"],
            name=file["name"],
            fract=file["fract"],
            mn=file["mn"],
            dmg=file["dmg"],
            hp=file["hp"],
            items=file["items"],
        )


def load_card_from_file(file: Path):
    card_dict = json.load(open(file))
    card_dict["id"] = file.stem
    lookup_table = {
        "unit": Unit.load,
        "item": Item.load,
        "location": Location.load,
        "event": Event.load,
    }
    card = lookup_table[card_dict["class"]](card_dict)
    return card


def load_cards(cards_path: Path):
    cards_list = listdir(cards_path)
    deck = dict()

    for card_file in map(Path, cards_list):
        full_path = cards_path / card_file
        if card_file.suffix != ".json" or not isfile(full_path):
            continue

        card = load_card_from_file(full_path)
        deck[card.id] = card
    return deck
