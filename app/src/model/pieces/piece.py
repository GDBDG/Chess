"""
different pieces
"""
from abc import ABC

from app.src.model.miscenaleous.color import Color


class Piece(ABC):
    """
    Abstract class for piece objects
    """

    def __init__(self, color: Color):
        """
        Constructor
        @param color: color of the piece
        """
        self.color = color

    def bit_value(self):
        """
        Return the bit value, used for the piece_dict hash
        @return: 1111 or 0111
        """
        return 0b1001 if self.color == Color.WHITE else 0b0001

    def __eq__(self, other):
        return type(self) == type(other) and self.color == other.color

    def __repr__(self):
        return "PI" if self.color == Color.WHITE else "pi"
