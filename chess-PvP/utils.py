from player import Player

def parse_position(pos):
    if pos == "out":
        return (-1, -1)
    if pos is None:
        return (None, None)

    x = ord(pos[0])
    y = ord(pos[1])
    return (56 - y, x - 97)


def is_checkmate(board):
    return False


def get_players():
    player_white = input("Name of player who takes white: ")
    player_black = input("Name of player who takes black: ")
    return [Player(player_white, "white"), Player(player_black, "black")]