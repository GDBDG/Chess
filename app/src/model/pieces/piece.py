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

    def __repr__(self):
        return "PI" if self.color == Color.WHITE else "pi"
