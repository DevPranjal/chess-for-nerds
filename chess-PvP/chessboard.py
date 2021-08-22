from piece import Piece


class ChessBoard:
    def __init__(self):
        self.white_king = Piece("king", "white", "e1")
        self.white_queen = Piece("queen", "white", "d1")
        self.white_bishop1 = Piece("bishop", "white", "c1")
        self.white_bishop2 = Piece("bishop", "white", "f1")
        self.white_knight1 = Piece("knight", "white", "b1")
        self.white_knight2 = Piece("knight", "white", "g1")
        self.white_rook1 = Piece("rook", "white", "a1")
        self.white_rook2 = Piece("rook", "white", "h1")
        self.white_pawn1 = Piece("pawn", "white", "a2")
        self.white_pawn2 = Piece("pawn", "white", "b2")
        self.white_pawn3 = Piece("pawn", "white", "c2")
        self.white_pawn4 = Piece("pawn", "white", "d2")
        self.white_pawn5 = Piece("pawn", "white", "e2")
        self.white_pawn6 = Piece("pawn", "white", "f2")
        self.white_pawn7 = Piece("pawn", "white", "g2")
        self.white_pawn8 = Piece("pawn", "white", "h2")

        self.black_king = Piece("king", "black", "e8")
        self.black_queen = Piece("queen", "black", "d8")
        self.black_bishop1 = Piece("bishop", "black", "c8")
        self.black_bishop2 = Piece("bishop", "black", "f8")
        self.black_knight1 = Piece("knight", "black", "b8")
        self.black_knight2 = Piece("knight", "black", "g8")
        self.black_rook1 = Piece("rook", "black", "a8")
        self.black_rook2 = Piece("rook", "black", "h8")
        self.black_pawn1 = Piece("pawn", "black", "a7")
        self.black_pawn2 = Piece("pawn", "black", "b7")
        self.black_pawn3 = Piece("pawn", "black", "c7")
        self.black_pawn4 = Piece("pawn", "black", "d7")
        self.black_pawn5 = Piece("pawn", "black", "e7")
        self.black_pawn6 = Piece("pawn", "black", "f7")
        self.black_pawn7 = Piece("pawn", "black", "g7")
        self.black_pawn8 = Piece("pawn", "black", "h7")

        self.recent_pos = (None, None)

    def make_board(self):
        empty = Piece()
        self.board = [[empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty],
                      [empty, empty, empty, empty, empty, empty, empty, empty]]

        R1_x, R1_y = parse_position(self.white_rook1.position)
        self.board[R1_x][R1_y] = self.white_rook1
        H1_x, H1_y = parse_position(self.white_knight1.position)
        self.board[H1_x][H1_y] = self.white_knight1
        B1_x, B1_y = parse_position(self.white_bishop1.position)
        self.board[B1_x][B1_y] = self.white_bishop1
        R2_x, R2_y = parse_position(self.white_rook2.position)
        self.board[R2_x][R2_y] = self.white_rook2
        H2_x, H2_y = parse_position(self.white_knight2.position)
        self.board[H2_x][H2_y] = self.white_knight2
        B2_x, B2_y = parse_position(self.white_bishop2.position)
        self.board[B2_x][B2_y] = self.white_bishop2
        K_x, K_y = parse_position(self.white_king.position)
        self.board[K_x][K_y] = self.white_king
        Q_x, Q_y = parse_position(self.white_queen.position)
        self.board[Q_x][Q_y] = self.white_queen
        P1_x, P1_y = parse_position(self.white_pawn1.position)
        self.board[P1_x][P1_y] = self.white_pawn1
        P2_x, P2_y = parse_position(self.white_pawn2.position)
        self.board[P2_x][P2_y] = self.white_pawn2
        P3_x, P3_y = parse_position(self.white_pawn3.position)
        self.board[P3_x][P3_y] = self.white_pawn3
        P4_x, P4_y = parse_position(self.white_pawn4.position)
        self.board[P4_x][P4_y] = self.white_pawn4
        P5_x, P5_y = parse_position(self.white_pawn5.position)
        self.board[P5_x][P5_y] = self.white_pawn5
        P6_x, P6_y = parse_position(self.white_pawn6.position)
        self.board[P6_x][P6_y] = self.white_pawn6
        P7_x, P7_y = parse_position(self.white_pawn7.position)
        self.board[P7_x][P7_y] = self.white_pawn7
        P8_x, P8_y = parse_position(self.white_pawn8.position)
        self.board[P8_x][P8_y] = self.white_pawn8

        r1_x, r1_y = parse_position(self.black_rook1.position)
        self.board[r1_x][r1_y] = self.black_rook1
        h1_x, h1_y = parse_position(self.black_knight1.position)
        self.board[h1_x][h1_y] = self.black_knight1
        b1_x, b1_y = parse_position(self.black_bishop1.position)
        self.board[b1_x][b1_y] = self.black_bishop1
        r2_x, r2_y = parse_position(self.black_rook2.position)
        self.board[r2_x][r2_y] = self.black_rook2
        h2_x, h2_y = parse_position(self.black_knight2.position)
        self.board[h2_x][h2_y] = self.black_knight2
        b2_x, b2_y = parse_position(self.black_bishop2.position)
        self.board[b2_x][b2_y] = self.black_bishop2
        k_x, k_y = parse_position(self.black_king.position)
        self.board[k_x][k_y] = self.black_king
        q_x, q_y = parse_position(self.black_queen.position)
        self.board[q_x][q_y] = self.black_queen
        p1_x, p1_y = parse_position(self.black_pawn1.position)
        self.board[p1_x][p1_y] = self.black_pawn1
        p2_x, p2_y = parse_position(self.black_pawn2.position)
        self.board[p2_x][p2_y] = self.black_pawn2
        p3_x, p3_y = parse_position(self.black_pawn3.position)
        self.board[p3_x][p3_y] = self.black_pawn3
        p4_x, p4_y = parse_position(self.black_pawn4.position)
        self.board[p4_x][p4_y] = self.black_pawn4
        p5_x, p5_y = parse_position(self.black_pawn5.position)
        self.board[p5_x][p5_y] = self.black_pawn5
        p6_x, p6_y = parse_position(self.black_pawn6.position)
        self.board[p6_x][p6_y] = self.black_pawn6
        p7_x, p7_y = parse_position(self.black_pawn7.position)
        self.board[p7_x][p7_y] = self.black_pawn7
        p8_x, p8_y = parse_position(self.black_pawn8.position)
        self.board[p8_x][p8_y] = self.black_pawn8

    def update_board(self, from_pos, to_pos):
        self.recent_pos = (from_pos, to_pos)

        from_x, from_y = parse_position(from_pos)
        to_x, to_y = parse_position(to_pos)

        self.board[to_x][to_y] = self.board[from_x][from_y]
        self.board[from_x][from_y].position = to_pos
        self.board[from_x][from_y] = Piece()

    def __str__(self):
        red_pos = [parse_position(self.recent_pos[0])]
        green_pos = [parse_position(self.recent_pos[1])]
        white_pos = [(0, 0), (0, 2), (0, 4), (0, 6),
                     (1, 1), (1, 3), (1, 5), (1, 7),
                     (2, 0), (2, 2), (2, 4), (2, 6),
                     (3, 1), (3, 3), (3, 5), (3, 7),
                     (4, 0), (4, 2), (4, 4), (4, 6),
                     (5, 1), (5, 3), (5, 5), (5, 7),
                     (6, 0), (6, 2), (6, 4), (6, 6),
                     (7, 1), (7, 3), (7, 5), (7, 7)]

        str_board = ""
        for i in range(8):
            str_board += f"  ---------------------------------\n{8 - i} |"
            for j in range(8):
                if (i, j) in red_pos:
                    str_board += '\x1b[6;37;41m' + " " + f"{self.board[i][j]}" + " " + '\x1b[0m' + "|"
                elif (i, j) in green_pos:
                    str_board += '\x1b[6;37;42m' + " " + f"{self.board[i][j]}" + " " + '\x1b[0m' + "|"
                elif (i, j) in white_pos:
                    str_board += '\x1b[1;30;47m' + " " + f"{self.board[i][j]}" + " " + '\x1b[0m' + "|"
                else:
                    str_board += '\x1b[2;37;40m' + " " + f"{self.board[i][j]}" + " " + '\x1b[0m' + "|"

                ##else:
                ##    if self.board[i][j].colour == "black":
                ##        str_board += " " + '\x1b[1;37;46m' + f"{self.board[i][j]}" + '\x1b[0m' + " |"
                ##    elif self.board[i][j].colour == "white":
                ##        str_board += " " + '\x1b[1;30;47m' + f"{self.board[i][j]}" + '\x1b[0m' + " |"
                ##    else:
                ##        str_board += f" {self.board[i][j]} |"
            str_board += "\n"
        str_board += "  ---------------------------------\n"
        str_board += "    a   b   c   d   e   f   g   h  "
        return str_board

    def print_board(self):
        print(self.__str__())


def parse_position(pos):
    if pos == "out":
        return (-1, -1)
    if pos is None:
        return (None, None)

    x = ord(pos[0])
    y = ord(pos[1])
    return (56 - y, x - 97)


if __name__ == "__main__":
    board = ChessBoard()
    board.make_board()
    print(board)
