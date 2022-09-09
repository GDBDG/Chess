"""
Bishop
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Bishop(Piece):
    """
    Bishop class
    """

    def __repr__(self):
        return "B" if self.color == Color.WHITE else "b"
