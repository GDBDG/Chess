"""
Knight
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Knight(Piece):
    """
    Knight class
    """

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1011 or 0011
        """
        return 0b1011 if self.color == Color.WHITE else 0b0011

    def __repr__(self):
        return "KN" if self.color == Color.WHITE else "kn"
