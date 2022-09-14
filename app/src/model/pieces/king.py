"""
King
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class King(Piece):
    """
    King class
    """

    def __repr__(self):
        return "K" if self.color == Color.WHITE else "k"
