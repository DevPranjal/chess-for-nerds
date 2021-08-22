from player import Player
from copy import deepcopy
from rules import validate_move


def is_check(from_pos, to_pos, player_to_move, board):
    board_cp = deepcopy(board)
    board_cp.update_board(from_pos, to_pos)
    result = False

    if player_to_move.colour == "black":
        player = Player("", "white")
        result = validate_move(board_cp.white_king.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_queen.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_bishop1.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_bishop2.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_knight1.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_knight2.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_rook1.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_rook2.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn1.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn2.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn3.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn4.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn5.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn6.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn7.position, board_cp.black_king.position, player, board_cp, True) or \
                validate_move(board_cp.white_pawn8.position, board_cp.black_king.position, player, board_cp, True)
            
    else:
        player = Player("", "black")
        result = validate_move(board_cp.black_king.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_queen.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_bishop1.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_bishop2.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_knight1.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_knight2.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_rook1.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_rook2.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn1.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn2.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn3.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn4.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn5.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn6.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn7.position, board_cp.white_king.position, player, board_cp, True) or \
                validate_move(board_cp.black_pawn8.position, board_cp.white_king.position, player, board_cp, True)

    if result:
        print("You are under check!")
    return result


def is_checkmate(board):
    return False


def get_players():
    player_white = input("Name of player who takes white: ")
    player_black = input("Name of player who takes black: ")
    return [Player(player_white, "white"), Player(player_black, "black")]