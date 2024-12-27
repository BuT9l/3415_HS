from src import gameserver
from pathlib import Path

from src.cards import load_card_from_file, load_cards
from src.resource import DECK


def __main__():
    # Можно добавить обработчик параметров коммандной строки, например --load <file>
    global DECK
    DECK = load_cards(Path("cards/"))
    server = gameserver.GameServer()
    server.run()


if __name__ == "__main__":
    __main__()
