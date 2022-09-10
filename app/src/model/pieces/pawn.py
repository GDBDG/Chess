"""
Pawn
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Pawn(Piece):
    """
    Pawn class
    """

    def __repr__(self):
        return "P" if self.color == Color.WHITE else "p"
