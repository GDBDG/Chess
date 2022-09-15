"""
Rook
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Rook(Piece):
    """
    Rook class
    """

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1110 or 0100
        """
        return 0b1110 if self.color == Color.WHITE else 0b0110

    def __repr__(self):
        return "R" if self.color == Color.WHITE else "r"
