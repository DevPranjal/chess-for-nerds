from chessboard import ChessBoard
from player import Player
import rules
from utils import is_checkmate
import os


def main():
    board = ChessBoard()
    board.make_board()

    player_black = Player("Pranjal", "black")
    player_white = Player("Yashika", "white")

    players = [player_white, player_black] ## [white, black]

    moves = 0

    while not is_checkmate(board):
        os.system("clear")
        print(board)

        player_to_move = players[moves%2]
        print(f"\n{player_to_move.name}, it is your turn to move")

        from_pos = input("Piece to move (position): ")
        to_pos = input("Where to move (position): ")

        while not rules.validate_move(from_pos, to_pos, player_to_move, board):
            print("Invalid move, please make another move.")
            from_pos = input("Piece to move (position): ")
            to_pos = input("Where to move (position): ")

        board.update_board(from_pos, to_pos)
        moves += 1


if __name__ == "__main__":
    main()