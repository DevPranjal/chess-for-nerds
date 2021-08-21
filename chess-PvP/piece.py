class Piece:
    def __init__(self, rank=None, colour=None, position=None):
        self.rank = rank
        self.colour = colour
        self.position = position

    def __str__(self):
        if self.rank == None and self.colour == None:
            return " "

        if self.rank == "king" and self.colour == "white":
            return "K"
        if self.rank == "queen" and self.colour == "white":
            return "Q"
        if self.rank == "bishop" and self.colour == "white":
            return "B"
        if self.rank == "knight" and self.colour == "white":
            return "H"
        if self.rank == "rook" and self.colour == "white":
            return "R"
        if self.rank == "pawn" and self.colour == "white":
            return "P"

        if self.rank == "king" and self.colour == "black":
            return "k"
        if self.rank == "queen" and self.colour == "black":
            return "q"
        if self.rank == "bishop" and self.colour == "black":
            return "b"
        if self.rank == "knight" and self.colour == "black":
            return "h"
        if self.rank == "rook" and self.colour == "black":
            return "r"
        if self.rank == "pawn" and self.colour == "black":
            return "p"