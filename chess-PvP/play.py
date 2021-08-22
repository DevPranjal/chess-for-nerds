from chessboard import ChessBoard
import rules
from utils import is_checkmate, is_check, get_players
import os


def main():
    board = ChessBoard()
    board.make_board()

    os.system("clear")
    print("Lets get started with your names: ")
    players = get_players()

    moves = 0

    while not is_checkmate(board):
        # Clear and print chessboard
        os.system("clear")
        print(board)

        # Decide player to move
        player_to_move = players[moves % 2]
        print(f"\n{player_to_move.name}, it is your turn to move")

        # Get input
        from_pos = input("Piece to move (position): ")
        to_pos = input("Where to move (position): ")

        # Validate against rules
        while not rules.validate_move(from_pos, to_pos, player_to_move, board):
            from_pos = input("Piece to move (position): ")
            to_pos = input("Where to move (position): ")

        # Check for the case of 'check' and if the player addresses it
        while is_check(from_pos, to_pos, player_to_move, board):
            from_pos = input("Piece to move (position): ")
            to_pos = input("Where to move (position): ")

        # Update positions
        board.update_board(from_pos, to_pos)
        moves += 1


if __name__ == "__main__":
    main()
