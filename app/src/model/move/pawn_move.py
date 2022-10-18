"""
Forward move (one square, no capture
"""
from app.src.model.game.board import Board
from app.src.model.game.square import Square
from app.src.model.move.move import Move


class PawnMove(Move):
    """
    Pawn move (one square, no capture)
    """

    def available_squares(self, origin: Square, board: Board):
        pass
