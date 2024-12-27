from src import gameserver
from pathlib import Path

from src.cards import load_card_from_file, load_cards


def __main__():
    # Можно добавить обработчик параметров коммандной строки, например --load <file>
    DECK = load_cards(Path("cards/"))
    server = gameserver.GameServer(DECK=DECK)
    server.run()


if __name__ == "__main__":
    __main__()
