"""
Bishop
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class Bishop(Piece):
    """
    Bishop class
    """

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1001 or 0001
        """
        return 0b1001 if self.color == Color.WHITE else 0b0001

    def __repr__(self):
        return "B" if self.color == Color.WHITE else "b"
