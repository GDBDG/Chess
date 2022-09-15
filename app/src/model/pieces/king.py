"""
King
"""
from app.src.model.miscenaleous.color import Color
from app.src.model.pieces.piece import Piece


class King(Piece):
    """
    King class
    """

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1010 or 0010
        """
        return 0b1010 if self.color == Color.WHITE else 0b0010

    def __repr__(self):
        return "K" if self.color == Color.WHITE else "k"
