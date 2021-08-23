from chessboard import parse_position


def validate_position_string(pos, comments_off=False):
    result = len(pos) == 2 and (97 <= ord(pos[0]) <= 104) and (49 <= ord(pos[1]) <= 56)
    if not result and not comments_off:
        print(f"Format of positions entered is wrong, please refer the docs.")

    return result


def rule1(from_pos, board, comments_off=False):
    """Initial position should contain a Piece"""
    x, y = parse_position(from_pos)
    result = board[x][y].rank != None
    if not result and not comments_off:
        print("Initial position should contain a Piece.")

    return result


def rule2(from_pos, player, board, comments_off=False):
    """Player should move his own piece"""
    x, y = parse_position(from_pos)
    result = player.colour == board[x][y].colour
    if not result and not comments_off:
        print("Player should move his own piece.")

    return result


def rule3(to_pos, player, board, comments_off=False):
    """Player should not take down his own piece"""
    x, y = parse_position(to_pos)
    result = player.colour != board[x][y].colour
    if not result and not comments_off:
        print("Player should not take down his own piece.")

    return result


def rules_pieces(from_pos, to_pos, board, comments_off=False):
    from_x, from_y = parse_position(from_pos)

    if board[from_x][from_y].rank == "king":
        return rules_king(from_pos, to_pos, board, comments_off)
    if board[from_x][from_y].rank == "queen":
        return rules_queen(from_pos, to_pos, board, comments_off)
    if board[from_x][from_y].rank == "bishop":
        return rules_bishop(from_pos, to_pos, board, comments_off)
    if board[from_x][from_y].rank == "knight":
        return rules_knight(from_pos, to_pos, board, comments_off)
    if board[from_x][from_y].rank == "rook":
        return rules_rook(from_pos, to_pos, board, comments_off)
    if board[from_x][from_y].rank == "pawn":
        return rules_pawn(from_pos, to_pos, board, comments_off)


def rules_king(from_pos, to_pos, board, comments_off=False):
    from_x, from_y = parse_position(from_pos)
    to_x, to_y = parse_position(to_pos)

    result = (abs(from_x - to_x) == 1 and from_y == to_y) or \
                (abs(from_y - to_y) == 1 and from_x == to_x) or \
                (abs(from_y - to_y) == 1 and abs(from_x - to_x) == 1)
    if not result and not comments_off:
        print("King move invalid, please refer to the docs or the game rules.")

    return result


def rules_queen(from_pos, to_pos, board, comments_off=False):
    result = rules_rook(from_pos, to_pos, board, True) or rules_bishop(from_pos, to_pos, board, True)
    if not result and not comments_off:
        print("Queen move invalid, please refer to the docs or the game rules.")
    return result


def rules_bishop(from_pos, to_pos, board, comments_off=False):
    from_x, from_y = parse_position(from_pos)
    to_x, to_y = parse_position(to_pos)

    # from_x > to_x and from_y > to_y OR to_x > from_x and to_y > from_y
    if abs(from_x - to_x) == abs(from_y - to_y) and (from_x - to_x) * (from_y - to_y) > 0:
        list_to_check_for_friendly_pieces = [(i, from_y - (from_x - i)) for i in range(min(from_x, to_x) + 1, max(from_x, to_x))]
        for pair in list_to_check_for_friendly_pieces:
            if board[pair[0]][pair[1]].rank != None:
                if not comments_off:
                    print("Bishop move invalid, please refer to the docs or the game rules.")
                return False

    # from_x > to_x and from_y < to_y OR to_x > from_x and to_y < from_y
    elif abs(from_x - to_x) == abs(from_y - to_y) and (from_x - to_x) * (from_y - to_y) < 0:
        list_to_check_for_friendly_pieces = [(i, from_y - (i - from_x)) for i in range(min(from_x, to_x) + 1, max(from_x, to_x))]
        for pair in list_to_check_for_friendly_pieces:
            if board[pair[0]][pair[1]].rank != None:
                if not comments_off:
                    print("Bishop move invalid, please refer to the docs or the game rules.")
                return False

    else:
        if not comments_off:
            print("Bishop move invalid, please refer to the docs or the game rules.")
        return False

    return True


def rules_knight(from_pos, to_pos, board, comments_off=False):
    from_x, from_y = parse_position(from_pos)
    to_x, to_y = parse_position(to_pos)

    result = (abs(from_x - to_x) == 1 and abs(from_y - to_y) == 2) or (abs(from_x - to_x) == 2 and abs(from_y - to_y) == 1)
    if not result and not comments_off:
        print("Knight move invalid, please refer to the docs or the game rules.")

    return result


def rules_rook(from_pos, to_pos, board, comments_off=False):
    from_x, from_y = parse_position(from_pos)
    to_x, to_y = parse_position(to_pos)

    if from_x == to_x:
        list_to_check_for_friendly_pieces = [i for i in range(min(from_y, to_y) + 1, max(from_y, to_y))]
        for y_pos in list_to_check_for_friendly_pieces:
            if board[to_x][y_pos].rank != None:
                if not comments_off:
                    print("Rook move invalid, please refer to the docs or the game rules.")
                return False

    elif from_y == to_y:
        list_to_check_for_friendly_pieces = [i for i in range(min(from_x, to_x) + 1, max(from_x, to_x))]
        for x_pos in list_to_check_for_friendly_pieces:
            if board[x_pos][to_y].rank != None:
                if not comments_off:
                    print("Rook move invalid, please refer to the docs or the game rules.")
                return False

    else:
        if not comments_off:
            print("Rook move invalid, please refer to the docs or the game rules.")
        return False

    return True


def rules_pawn(from_pos, to_pos, board, comments_off=False):
    from_x, from_y = parse_position(from_pos)
    to_x, to_y = parse_position(to_pos)

    # First check if 
    if (board[from_x][from_y].colour == "black" and ((from_x == 1 and to_x == 3 and from_y == to_y) or to_x - from_x == 1)) or \
        (board[from_x][from_y].colour == "white" and ((from_x == 6 and to_x == 4 and from_y == to_y) or from_x - to_x == 1)):

        if board[to_x][to_y].colour != None and board[to_x][to_y].colour != board[from_x][from_y].colour:
            if abs(from_y - to_y) == 1 and abs(from_x - to_x) == 1:
                # Pawn can capture in diagonal direction
                return True

            else:
                # Pawn cannot capture in straight direction
                if not comments_off:
                    print(f"Pawn move invalid, please refer to the docs or the game rules.")
                return False

        if to_y == from_y:
            return True

    if not comments_off:
        print(f"Pawn move invalid, please refer to the docs or the game rules.")
    return False


def validate_move(from_pos, to_pos, player, board, comments_off=False):
    return validate_position_string(from_pos, comments_off) and \
            validate_position_string(to_pos, comments_off) and \
            rule1(from_pos, board.board, comments_off) and \
            rule2(from_pos, player, board.board, comments_off) and \
            rule3(to_pos, player, board.board, comments_off) and \
            rules_pieces(from_pos, to_pos, board.board, comments_off)
