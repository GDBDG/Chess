"""
Knight
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Knight(Piece):
    """
    Knight class
    """

    def __repr__(self):
        return "KN" if self.color == Color.WHITE else "kn"
