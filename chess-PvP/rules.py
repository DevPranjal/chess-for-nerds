class Rules:
    def __init__(self):
        pass

    def rule1(self, player, move):
        """Player should move his own piece"""
        return player.colour == move.piece.colour

    def validate_move(self, player, move, board):
        pass