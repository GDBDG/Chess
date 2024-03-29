"""
Pawn
"""
from app.src.model.classes.const.color import Color
from app.src.model.classes.pieces.piece import Piece


class Pawn(Piece):
    """
    Pawn classes
    """

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1100 or 0100
        """
        return 0b1100 if self.color == Color.WHITE else 0b0100

    def __repr__(self):
        return "P" if self.color == Color.WHITE else "p"
