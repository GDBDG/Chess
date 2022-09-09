"""
Queen
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Queen(Piece):
    """
    Queen class
    """

    def __repr__(self):
        return "Q" if self.color == Color.WHITE else "q"
