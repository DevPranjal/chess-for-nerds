from utils import parse_position


def validate_position_string(pos):
    result = len(pos) == 2 and (97 <= ord(pos[0]) <= 104) and (49 <= ord(pos[1]) <= 56)
    if not result:
        print(f"Format of positions entered is wrong, please refer the docs.{ord(pos[1])}")

    return result


def rule1(from_pos, board):
    """Initial position should contain a Piece"""
    x, y = parse_position(from_pos)
    result = board[x][y].rank != None
    if not result:
        print("Initial position should contain a Piece.")

    return result


def rule2(from_pos, player, board):
    """Player should move his own piece"""
    x, y = parse_position(from_pos)
    result = player.colour == board[x][y].colour
    if not result:
        print("Player should move his own piece.")

    return result


def rule3(to_pos, player, board):
    """Player should not take down his own piece"""
    x, y = parse_position(to_pos)
    result = player.colour != board[x][y].colour
    if not result:
        print("Player should not take down his own piece.")

    return result





def validate_move(from_pos, to_pos, player, board):
    return validate_position_string(from_pos) and \
            validate_position_string(to_pos) and \
            rule1(from_pos, board) and \
            rule2(from_pos, player, board) and \
            rule3(to_pos, player, board)
