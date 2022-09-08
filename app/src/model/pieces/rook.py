"""
Rook
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Rook(Piece):
    """
    Rook class
    """

    def __repr__(self):
        return "R" if self.color == Color.WHITE else "r"
