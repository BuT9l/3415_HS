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
    def load(cls, card_dict):
        return cls(
            id=card_dict["id"],
            name=card_dict["name"],
            fract=card_dict["fract"],
            mn=card_dict["mn"],
        )

    def save(self):
        d = dict()
        d["id"] = self.id
        d["name"] = self.name
        d["fract"] = self.fract
        d["mn"] = self.mn
        return d


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
    def load(cls, card_dict):
        return cls(
            id=card_dict["id"],
            name=card_dict["name"],
            fract=card_dict["fract"],
            mn=card_dict["mn"],
            dmg_boost=card_dict["dmg_boost"],
            hp_boost=card_dict["hp_boost"],
        )

    def save(self):
        d = super().save()
        d["dmg_boost"] = self.dmg_boost
        d["hp_boost"] = self.hp_boost
        return d


class Unit(Card):
    def __init__(self, id, name, fract, mn, dmg, hp, items):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)
        self.dmg = dmg
        self.hp = hp
        self.items = items if items is not None else list()

    @classmethod
    def load(cls, card_dict):
        return cls(
            id=card_dict["id"],
            name=card_dict["name"],
            fract=card_dict["fract"],
            mn=card_dict["mn"],
            dmg=card_dict["dmg"],
            hp=card_dict["hp"],
            items=card_dict.get("items"),
            # get() will return None if items does not exist, and they does not in plain cards from repo
        )

    def save(self):
        d = super().save()
        d["dmg"] = self.dmg
        d["hp"] = self.hp
        d["items"] = self.items
        return d

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
    def load(cls, card_dict):
        return cls(
            id=card_dict["id"],
            name=card_dict["name"],
            fract=card_dict["fract"],
            mn=card_dict["mn"],
            dmg_boost=card_dict["dmg_boost"],
            hp_boost=card_dict["hp_boost"],
        )

    def save(self):
        d = super().save()
        d["dmg_boost"] = self.dmg_boost
        d["hp_boost"] = self.hp_boost
        return d


class Event(Card):
    def __init__(self, id, name, fract, mn):
        Card.__init__(self, id=id, name=name, fract=fract, mn=mn)

    @classmethod
    def load(cls, card_dict):
        return cls(
            id=card_dict["id"],
            name=card_dict["name"],
            fract=card_dict["fract"],
            mn=card_dict["mn"],
        )

    def save(self):
        d = super().save()
        return d


class PlayerUnit(Unit):
    def __init__(self, id, name, fract, mn, dmg, hp, items):
        super().__init__(
            id=id, name=name, fract=fract, mn=mn, dmg=dmg, hp=hp, items=items
        )

    @classmethod
    def load(cls, card_dict):
        return cls(
            id=card_dict["id"],
            name=card_dict["name"],
            fract=card_dict["fract"],
            mn=card_dict["mn"],
            dmg=card_dict["dmg"],
            hp=card_dict["hp"],
            items=card_dict.get("items"),
        )

    def save(self):
        d = super().save()
        d["dmg"] = self.dmg
        d["hp"] = self.hp
        d["items"] = self.items
        return d


def load_card_from_file(file: Path):
    card_dict = json.load(open(file))
    card_dict["id"] = file.stem
    lookup_table = {
        "unit": Unit.load,
        "item": Item.load,
        "location": Location.load,
        "event": Event.load,
        "player": PlayerUnit.load,
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
